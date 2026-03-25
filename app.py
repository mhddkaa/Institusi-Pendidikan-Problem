import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Prediksi Dropout Siswa", layout="wide")

# Load model
model = joblib.load('random_forest_model.pkl')

st.title("👨‍🎓 Prediksi Dropout Siswa 👩‍🎓")
st.markdown("Aplikasi ini akan memprediksi apakah siswa berpotensi **Dropout** atau **Graduate** berdasarkan data akademik dan demografi.")

# Mapping untuk fitur kategorikal
marital_map = {
    'Single': 1, 'Married': 2, 'Widower': 3,
    'Divorced': 4, 'Facto Union': 5, 'Legally Separated': 6
}

gender_map = {'Female': 0, 'Male': 1}
yes_no_map = {'No': 0, 'Yes': 1} 

application_mode_map = {
    "1 - General Phase 1": 1,
    "2 - Ordinance 612/93": 2,
    "5 - Special Contingent (Azores)": 5,
    "7 - Other Higher Course Holders": 7,
    "10 - Ordinance 854-B/99": 10,
    "15 - International Student": 15,
    "16 - Special Contingent (Madeira)": 16,
    "17 - General Phase 2 (Recommended)": 17,
    "18 - General Phase 3": 18,
    "26 - Ordinance 533-A/99 (b2)": 26,
    "27 - Ordinance 533-A/99 (b3)": 27,
    "39 - Over 23 Years Old": 39,
    "42 - Transfer": 42,
    "43 - Change of Course": 43,
    "44 - Tech Specialization Diploma": 44,
    "51 - Change Institution/Course": 51,
    "53 - Short Cycle Diploma": 53,
    "57 - International Transfer": 57
}

# Layout dengan 2 kolom
col1, col2 = st.columns(2)

# Kolom 1
with col1:
    st.subheader("🧍 Data Pribadi")

    Marital_status_label = st.selectbox(
        "Marital Status",
        list(marital_map.keys()),
        help="Status pernikahan siswa"
    )
    Marital_status = marital_map[Marital_status_label] 

    Gender_label = st.selectbox(
        "Gender",
        list(gender_map.keys()),
        help="Jenis kelamin siswa"
    )
    Gender = gender_map[Gender_label]

    Age_at_enrollment = st.number_input(
        "Age at Enrollment",
        17, 70, 20,
        help="Umur saat pertama masuk kuliah"
    )

    st.subheader("📚 Akademik Awal")

    Application_mode_label = st.selectbox(
        "Application Mode",
        list(application_mode_map.keys()),
        index=7, 
        help="Pilih jalur masuk siswa. Gunakan 'General Phase 2 (17)' jika tidak yakin"
    )
    Application_mode = application_mode_map[Application_mode_label]

    Previous_qualification_grade = st.number_input(
        "Previous Qualification Grade",
        95.0, 190.0, 130.0,
        help="Nilai pendidikan sebelumnya"
    )

    Admission_grade = st.number_input(
        "Admission Grade",
        95.0, 190.0, 125.0,
        help="Nilai saat seleksi masuk"
    )

    st.subheader("💰 Status Finansial")

    Displaced = yes_no_map[
        st.selectbox("Displaced", list(yes_no_map.keys()),
        help="Apakah tinggal jauh dari rumah")
    ]

    Debtor = yes_no_map[
        st.selectbox("Debtor", list(yes_no_map.keys()),
        help="Memiliki tunggakan pembayaran")
    ]

    Tuition_fees_up_to_date = yes_no_map[
        st.selectbox("Tuition Fees Up To Date", list(yes_no_map.keys()),
        help="Status pembayaran kuliah")
    ]

    Scholarship_holder = yes_no_map[
        st.selectbox("Scholarship Holder", list(yes_no_map.keys()),
        help="Penerima beasiswa")
    ]

# Kolom 2
with col2:
    st.subheader("📊 Performa Semester 1")

    Curricular_units_1st_sem_enrolled = st.number_input(
        "Enrolled (Sem 1)", 0, 30, 6
    )

    Curricular_units_1st_sem_approved = st.number_input(
        "Approved (Sem 1)", 0, 30, 5
    )

    Curricular_units_1st_sem_grade = st.number_input(
        "Grade (Sem 1)", 0.0, 20.0, 12.0
    )

    st.subheader("📊 Performa Semester 2")

    Curricular_units_2nd_sem_enrolled = st.number_input(
        "Enrolled (Sem 2)", 0, 30, 6
    )

    Curricular_units_2nd_sem_evaluations = st.number_input(
        "Evaluations (Sem 2)", 0, 40, 8
    )

    Curricular_units_2nd_sem_approved = st.number_input(
        "Approved (Sem 2)", 0, 30, 5
    )

    Curricular_units_2nd_sem_grade = st.number_input(
        "Grade (Sem 2)", 0.0, 20.0, 12.0
    )

    Curricular_units_2nd_sem_without_evaluations = st.number_input(
        "Without Evaluations (Sem 2)", 0, 15, 0
    )

# Validasi input
if Curricular_units_1st_sem_approved > Curricular_units_1st_sem_enrolled:
    st.warning("⚠️ Approved Semester 1 tidak boleh lebih besar dari Enrolled")

if Curricular_units_2nd_sem_approved > Curricular_units_2nd_sem_enrolled:
    st.warning("⚠️ Approved Semester 2 tidak boleh lebih besar dari Enrolled")

# Prediksi
if st.button("🔍 Prediksi"):

    input_data = np.array([[
        Marital_status,
        Application_mode,
        Previous_qualification_grade,
        Admission_grade,
        Displaced,
        Debtor,
        Tuition_fees_up_to_date,
        Gender,
        Scholarship_holder,
        Age_at_enrollment,
        Curricular_units_1st_sem_enrolled,
        Curricular_units_1st_sem_approved,
        Curricular_units_1st_sem_grade,
        Curricular_units_2nd_sem_enrolled,
        Curricular_units_2nd_sem_evaluations,
        Curricular_units_2nd_sem_approved,
        Curricular_units_2nd_sem_grade,
        Curricular_units_2nd_sem_without_evaluations
    ]])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    st.subheader("Hasil Prediksi")

    if prediction == 0:
        st.error("Siswa berpotensi Dropout")
    else:
        st.success("Siswa berpotensi Graduate")

    st.write("### Probabilitas:")
    st.write(f"Dropout: {proba[0]*100:.2f}%")
    st.write(f"Graduate: {proba[1]*100:.2f}%")
