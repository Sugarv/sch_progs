# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import RegexValidator


class Program(models.Model):
    EIDIKOTHTES = [
      ('ΠΕ60','ΠΕ60 Νηπιαγωγών'),
      ('ΠΕ70','ΠΕ70 Δασκάλων'),
      ('ΠΕ05','ΠΕ05 Γαλλικών'),
      ('ΠΕ06','ΠΕ06 Αγγλικών'),
      ('ΠΕ07','ΠΕ07 Γερμανικών'),
      ('ΠΕ08','ΠΕ08 Καλλιτεχνικών'),
      ('ΠΕ11','ΠΕ11 Φυσικής αγωγής'),
      ('ΠΕ79','ΠΕ79 Μουσικών'),
      ("ΠΕ23","Ψυχολόγων"),
      ("ΠΕ26","Λογοθεραπευτών"),
      ("ΠΕ28","Φυσικοθεραπευτών"),
      ("ΠΕ86","Πληροφορικής"),
      ("ΠΕ30","Κοιν.Λειτουργών"),
      ("ΔΕ1ΕΒΠ","Βοηθ.Προσ.Ειδ.Αγ."),
      ("ΠΕ60ΕΑΕ","Νηπιαγωγών Ειδ.Αγ."),
      ("ΠΕ61","Νηπιαγωγών Ειδ.Αγ."),
      ("ΠΕ70ΕΑΕ","Δασκάλων Ειδ.Αγωγ."),
      ("ΠΕ71","Δασκάλων Ειδ.Αγωγ."),
      ("ΠΕ91","Θεατρικών Σπουδών"),
      ("ΠΕ25","Σχ.Νοσηλευτών"),
      ("ΠΕ21","Λογοθεραπευτών"),
      ("ΠΕ29","Εργοθεραπευτών"),
      ("ΤΕ16","Μουσικών Τ.Ε."),
    ]
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Ο αρ. τηλεφώνου πρέπει να είναι αριθμός με 10 ψηφία.")
    
    #sch1 = models.IntegerField()
    school1 = models.ForeignKey('School',on_delete=models.CASCADE, verbose_name='Σχολείο')
    sch_head1 = models.CharField('Ον/μο Δ/ντή/-ντριας',max_length=100)
    #sch2 = models.IntegerField()
    #sch2 = models.ForeignKey('Schools',on_delete=models.CASCADE)
    #princ2 = models.CharField(max_length=100)
    name1 = models.CharField('Όνοματεπώνυμο Συντονιστή/τριας', max_length=100)
    email1 = models.EmailField('email Συντονιστή/τριας', blank=True)
    mobile1 = models.CharField('Κινητό τηλέφωνο Συντονιστή/τριας',validators=[phone_regex], max_length=10, blank=True)
    eidikothta1 = models.CharField('Ειδικότητα Συντονιστή/τριας', max_length=40,choices=EIDIKOTHTES)
    history1 = models.CharField('Υλοποίηση προγραμμάτων Συντονιστή/τριας στο παρελθόν',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    qual1 = models.CharField('Επιμόρφωση Συντονιστή/τριας',max_length=3,choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    name2 = models.CharField('Όνοματεπώνυμο 2ου εκπ/κού', max_length=100)
    email2 = models.EmailField('email 2ου εκπ/κού', blank=True)
    mobile2 = models.CharField('Κινητό τηλέφωνο 2ου εκπ/κού',validators=[phone_regex], max_length=10, blank=True)
    eidikothta2 = models.CharField('Ειδικότητα 2ου εκπ/κού',max_length=40,choices=EIDIKOTHTES)
    history2 = models.CharField('Υλοποίηση προγραμμάτων 2ου εκπ/κού στο παρελθόν',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    qual2 = models.CharField('Επιμόρφωση 2ου εκπ/κού',max_length=3,choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    name3 = models.CharField('Όνοματεπώνυμο 3ου εκπ/κού', max_length=100, blank=True)
    email3 = models.EmailField('email 3ου εκπ/κού', blank=True)
    mobile3 = models.CharField('Κινητό τηλέφωνο 3ου εκπ/κού',validators=[phone_regex], max_length=10, blank=True)
    eidikothta3 = models.CharField('Ειδικότητα 3ου εκπ/κού',max_length=40,choices=EIDIKOTHTES, blank=True)
    history3 = models.CharField('Υλοποίηση προγραμμάτων 3ου εκπ/κού στο παρελθόν',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    qual3 = models.CharField('Επιμόρφωση 3ου εκπ/κού',max_length=3,choices=[('Ναι','Ναι'),('Όχι','Όχι')], blank=True)
    title = models.TextField('Τίτλος προγράμματος')
    category = models.CharField('Κατηγορία προγράμματος',max_length=27,choices=[
      ('Αγωγής Υγείας','Αγωγής Υγείας'),
      ('Περιβαλλοντικής Εκπαίδευσης', 'Περιβαλλοντικής Εκπαίδευσης'),
      ('Πολιτιστικών Θεμάτων','Πολιτιστικών Θεμάτων')
      ])
    praxi = models.IntegerField('Πράξη ανάθεσης')
    praxidate = models.DateField('Ημ/νία πράξης')
    tmimata = models.TextField('Τμήμα/τμήματα')
    students_nr = models.IntegerField( 'Αριθμός Μαθητών')
    students_nr_boys = models.IntegerField('Αριθμός αγοριών', blank=True)
    students_nr_girls = models.IntegerField('Αριθμός κοριτσιών', blank=True)
    chars = models.CharField('Χαρακτηριστικά ομάδας',max_length=12, choices=[
      ('Μικτή ομάδα','Μικτή ομάδα'),('Αμιγές τμήμα','Αμιγές τμήμα')
    ])
    arxeio = models.CharField('Ύπαρξη αρχείου Σχολικών Δραστηριοτήτων στο Σχολείο',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')])
    theme = models.TextField('Κύριο θέμα - Θεματικές Ενότητες')
    goal = models.TextField('Παιδαγωγικοί στόχοι')
    methodology = models.TextField('Μεθοδολογία Υλοποίησης')
    duration = models.CharField('Προβλεπόμενη διάρκεια προγράμματος (μήνες)', max_length=7, choices=[
      ('2 μήνες','2 μήνες'),('3 μήνες','3 μήνες'),('4 μήνες','4 μήνες'),('5 μήνες','5 μήνες')
    ])
    month = models.CharField('Μήνας έναρξης',max_length=20, blank=True)
    visits = models.TextField('Αριθμός προβλεπόμενων επισκέψεων - Συνεργασίες με άλλους φορείς', blank=True)
    foreis = models.TextField('Φορείς επισκέψεων', blank=True)
    pedia = models.TextField('Πεδία σύνδεσης με τα προγράμματα σπουδών των αντίστοιχων γνωστικών αντικειμένων', blank=True)
    diaxysh = models.CharField('Τρόποι διάχυσης',max_length=136,choices=[
      ('Έντυπη έκδοση','Έντυπη έκδοση'),
      ('Αναρτήσεις στο διαδίκτυο','Αναρτήσεις στο διαδίκτυο'),
      ('Παραγωγή βίντεο','Παραγωγή βίντεο'),
      ('Αφίσες - φυλλάδια','Αφίσες - φυλλάδια'),
      ('Έκθεση κατασκευών - χειροτεχνιών - φωτογραφιών','Έκθεση κατασκευών - χειροτεχνιών - φωτογραφιών'),
      ('Παρεμβάσεις','Παρεμβάσεις'),
      ('Άλλο','Άλλο')
    ], blank=True)
    diaxysh_other = models.TextField('Άλλοι τρόποι διάχυσης', blank=True)
    mon1 = models.TextField('1ος Μήνας', blank=True)
    mon2 = models.TextField('2ος Μήνας', blank=True)
    mon3 = models.TextField('3ος Μήνας', blank=True)
    mon4 = models.TextField('4ος Μήνας', blank=True)
    mon5 = models.TextField('5ος Μήνας', blank=True)
    prsnt = models.CharField('Πρόθεση παρουσίασης προγράμματος σε εκδήλωση', max_length=4, choices=[('Ναι','Ναι'),('Ίσως','Ίσως'),('Όχι','Όχι')])
    notes = models.TextField('Τυχόν παρατηρήσεις-επισημάνσεις', blank=True)
    checked = models.CharField('Βεβαιώνεται ότι ο/η δ/ντής/τρια ή προϊσταμένος/νη της σχολικής μονάδας έλεγξε το παρόν σχέδιο προγράμματος σχολικών δραστηριοτήτων, έκανε απαραίτητες τυχόν διορθώσεις και βεβαιώνει ότι τα στοιχεία που αναφέρονται στο παρόν σχέδιο προγράμματος είναι σωστά.',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')])
    vev = models.CharField('Ο/Η  δ/ντής/τρια ή προϊσταμένος/νη βεβαιώνει ότι το συγκεκριμένο σχέδιο προγράμματος σχολικών δραστηριοτήτων ολοκληρώθηκε επιτυχώς και τα αποτελέσματα του προγράμματος είναι διαθέσιμα στο σχολική μονάδα.',max_length=3, choices=[('Ναι','Ναι'),('Όχι','Όχι')])
    timestamp = models.DateTimeField('Τελ.Ενημέρωση',auto_now=True, editable=False)

    def __str__(self):
        return self.title



class School(models.Model):
    code_regex = RegexValidator(regex=r'^\d{7}$', message="Ο κωδικός ΥΠΑΙΘ πρέπει να είναι αριθμός με 7 ψηφία.")
    name = models.CharField('Όνομα σχολικής μονάδας',max_length=100)
    code = models.CharField('Κωδικός ΥΠΑΙΘ',validators=[code_regex], max_length=7, blank=True)
    type = models.CharField('Τύπος',max_length=20,choices=[
      ('Δημοτικό','Δημοτικό σχολείο'),
      ('Νηπιαγωγείο','Νηπιαγωγείο')
    ])
    email = models.EmailField('E-mail',max_length=50)
    dimos = models.CharField('Δήμος',max_length=50)
    tel = models.CharField('Τηλέφωνο',max_length=40)

    def __str__(self):
        return self.name
