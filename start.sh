if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/KarunaTG/Priyanka.git /Priyanka
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Priyanka
fi
cd /Nataliya
pip3 install -U -r requirements.txt
echo "Starting Priyanka...."
python3 bot.py
