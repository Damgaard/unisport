Product Displayer 2000
======================

Solution to the unisport sample task.
https://github.com/unisport/sample

Setting up
----------

To set up the project run the following command.

.. code-block:: bash

   git clone git@github.com:Damgaard/unisport.git
   cd unisport
   virtualenv virtualenv
   source virtualenv/bin/activate
   pip install -r project/requirements.txt
   ./manage.py migrate --noinput
   python fetch_initial_data.py
   ./manage.py loaddata sample.json
   ./manage.py createsuperuser

As part of the process you will be asked to create a superuser. This is the
useraccount you will need to add/change/delete produccts in Djangos admin
backend.

Dev details
-----------

This sample was built using python 2.7.6 on Ubuntu 14.04, it was not tested
on other machines.

Testing
-------

To test, run

.. code-block:: bash

    ./manage.py test

Author
------

Andreas Damgaard Pedersen
andreas.damgaard.p@gmail.com
