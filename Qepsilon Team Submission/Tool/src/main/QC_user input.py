from app.src.main.pipelines.quantum import send_into_quantum_pipeline

QCsentence = input("Please type your sentence: ")
send_into_quantum_pipeline(QCsentence)
