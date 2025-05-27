using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace parallaxscrolling
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.DoubleBuffered = true;
        }
        //defining image property names
        Image layer_1 = Properties.Resources.sprite_1;
        Image layer_2 = Properties.Resources.sprite_2;
        Image layer_3 = Properties.Resources.sprite_3;

        //creating int variable names/values to calculate
        //width of sprites
        int b1 = 0, b2 = 677, x1 = 0, x2 = 677, g1 = 0, g2 = 677;

        private void timer1_Tick(object sender, EventArgs e)
        {
            background_move();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //boolean names/values for player & background 
        //movement
        bool right, hold = true;

        //function for background parallax movement
        void background_move()
        {
            //if b1 layer_1 left is less than -677
            //set b1 left to 670
            if(b1<-677)
            {
                b1 = 670;
            }
            //if right arrow key pressed
            //move b1,b2 layer_1 img from right to left
            //speed of 2
            if(right)
            {
                b1 -= 2;
                b2 -= 2;
            }
            //b2 layer_1 left is < -677
            //set b2 left =670 and invalidate
            if(b2 < -677)
            {
                b2 = 670;
            }

            if (x1 < -677)
            {
                x1 = 670;
            }
            if(right)
            {
                x1 -= 4;
                x2 -= 4;
            }
            if(x2 < -677)
            {
                x2 = 670;
            }
            if(g1 < -677)
            {
                g1 = 670;
            }
            if(right)
            {
                g1 -= 5;
                g2 -= 5;
            }
            if (g2 < -677)
            {
                g2 = 670;
            }
            Invalidate();
        }


        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            if(e.KeyCode ==Keys.Right&!hold)
            {
                right = false;
                hold = true;
                player.Image = Properties.Resources.ideal_right_img;
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if(e.KeyCode == Keys.Right&hold)
            {
                right = true;
                hold = false;
                player.Image = Properties.Resources.run_right_img;
            }
        }


        //paint event section - where all layers drawn 
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //code to draw (b1) layer_1 img
            //arrange layer and sequence here
            e.Graphics.DrawImage(layer_1, b1,0);
            e.Graphics.DrawImage(layer_1, b2, 0);
            e.Graphics.DrawImage(layer_2, x1, 0);
            e.Graphics.DrawImage(layer_2, x2, 0);
            e.Graphics.DrawImage(layer_3, g1, 0);
            e.Graphics.DrawImage(layer_3, g2, 0);

        }
    }
}
