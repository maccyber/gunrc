GunRC - GTK Universal Network Remote Control
============================================

.. image:: https://github.com/maccyber/gunrc/screenshot.png

(#features)

A GTK-3 remote control for network-connected devices such as:

* Recivers
* Decoders
* Televisions

It uses a XML-based template system, so it's easy to add devices and functions.

Currently it supports:

* Pioneer VSX-series Reciver
	+ Turn "Network Standby" on
* Enigma devices such as dreambox, vuplus etc

Using GunRC
============

Requirements
------------

In order to run GunRC, you will need the following dependencies:

* Python >= 3.2
* `PyGObject`_ (aka Python GObject Introspection) (3.7.4 or more recommended,
  earlier versions may also work)
* GTK >= 3.4

.. _PyGObject: https://live.gnome.org/PyGObject

GunRC can currently be downloaded from the Git repository using::

    $ git clone git://github.com/maccyber/gunrc.git
    $ cd gunrc

To run GunRC, you can install it in a dedicated directory (as root)::

    # python setup.py install
