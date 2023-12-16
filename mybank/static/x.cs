using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// Entity Framework'ü kullanmak için gerekli using direktifi
using WindowsFormsApp6.Models;

namespace WindowsFormsApp6
{
    public partial class Form1 : Form
    {
        // Veritabanı bağlantısı için DbContext
        DbStudentEntities Db = new DbStudentEntities();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnList_Click(object sender, EventArgs e)
        {
            // Öğrenci listesini DataGridView'e yükler
            var query = from x in Db.Students
                        select new
                        {
                            x.Id,
                            x.FirstName,
                            x.LastName,
                            x.PhoneNumber
                        };
            dataGridView1.DataSource = query.ToList();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            // Yeni öğrenci ekler
            Student student = new Student();
            student.FirstName = txtFirstName.Text;
            student.LastName = txtLastName.Text;
            student.PhoneNumber = txtPhoneNumber.Text;
            Db.Students.Add(student);
            Db.SaveChanges();
            MessageBox.Show("Process Completed...");
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            // Seçilen öğrenciyi siler
            int id = Convert.ToInt16(txtId.Text);
            Student student = Db.Students.Find(id);
            Db.Students.Remove(student);
            Db.SaveChanges();
            MessageBox.Show("Process Completed...");
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            // Seçilen öğrencinin bilgilerini günceller
            int id = Convert.ToInt16(txtId.Text);
            Student student = Db.Students.Find(id);
            student.FirstName = txtFirstName.Text;
            student.LastName = txtLastName.Text;
            student.PhoneNumber = txtPhoneNumber.Text;
            Db.SaveChanges();
        }

        private void dataGridView1_CellClick(object sender, 
        DataGridViewCellEventArgs e)
        {
            // DataGridView'de bir hücreye tıklandığında ilgili
            // öğrenci bilgilerini TextBox'lara yükler
            txtId.Text = dataGridView1.Rows[e.RowIndex].Cells[0]
            .Value.ToString();
            txtFirstName.Text = dataGridView1.Rows[e.RowIndex].Cells[1]
            .Value.ToString();
            txtLastName.Text = dataGridView1.Rows[e.RowIndex].Cells[2]
            .Value.ToString();
            txtPhoneNumber.Text = dataGridView1.Rows[e.RowIndex].Cells[3]
            .Value.ToString();
        }

        private void btnNoteList_Click(object sender, EventArgs e)
        {
            // Not listesini DataGridView'e yükler
            var query = from x in Db.Notes
                        select new
                        {
                            x.Student.FirstName,
                            x.Student.LastName,
                            x.Lesson.LessonName,
                            x.Exam1,
                            x.Exam2,
                            x.Average
                        };
            dataGridView1.DataSource = query.ToList();
        }
    }
}
