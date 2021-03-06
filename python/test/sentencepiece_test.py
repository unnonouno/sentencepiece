#!/usr/bin/python
# -*- coding: utf-8 -*-

import sentencepiece as spm
import unittest

class TestSentencepieceProcessor(unittest.TestCase):
    """Test case for SentencePieceProcessor"""

    def setUp(self):
        self.sp_ = spm.SentencePieceProcessor()
        self.assertTrue(self.sp_.Load('test/test_model.model'))
        self.jasp_ = spm.SentencePieceProcessor()
        self.assertTrue(self.jasp_.Load('test/test_ja_model.model'))

    def test_load(self):
        self.assertEqual(1000, self.sp_.GetPieceSize())
        self.assertEqual(0, self.sp_.PieceToId('<unk>'))
        self.assertEqual(1, self.sp_.PieceToId('<s>'))
        self.assertEqual(2, self.sp_.PieceToId('</s>'))
        self.assertEqual('<unk>', self.sp_.IdToPiece(0))
        self.assertEqual('<s>', self.sp_.IdToPiece(1))
        self.assertEqual('</s>', self.sp_.IdToPiece(2))
        for i in range(self.sp_.GetPieceSize()):
            piece = self.sp_.IdToPiece(i)
            self.assertEqual(i, self.sp_.PieceToId(piece))

    def test_roundtrip(self):
        text = 'I saw a girl with a telescope.'
        ids = self.sp_.EncodeAsIds(text)
        pieces1 = self.sp_.EncodeAsPieces(text)
        pieces2 = self.sp_.Encode(text)
        self.assertEqual(pieces1, pieces2)
        self.assertEqual(text, self.sp_.Decode(pieces1))
        self.assertEqual(text, self.sp_.DecodePieces(pieces2))
        self.assertEqual(text, self.sp_.DecodeIds(ids))

    def test_ja_load(self):
        self.assertEqual(8000, self.jasp_.GetPieceSize())
        self.assertEqual(0, self.jasp_.PieceToId('<unk>'))
        self.assertEqual(1, self.jasp_.PieceToId('<s>'))
        self.assertEqual(2, self.jasp_.PieceToId('</s>'))
        self.assertEqual('<unk>', self.jasp_.IdToPiece(0))
        self.assertEqual('<s>', self.jasp_.IdToPiece(1))
        self.assertEqual('</s>', self.jasp_.IdToPiece(2))
        for i in range(self.jasp_.GetPieceSize()):
            piece = self.jasp_.IdToPiece(i)
            self.assertEqual(i, self.jasp_.PieceToId(piece))

    def test_ja_roundtrip(self):
        text = '清水寺は京都にある。'
        ids = self.jasp_.EncodeAsIds(text)
        pieces1 = self.jasp_.EncodeAsPieces(text)
        pieces2 = self.jasp_.Encode(text)
        self.assertEqual(pieces1, pieces2)
        self.assertEqual(text, self.jasp_.Decode(pieces1))
        self.assertEqual(text, self.jasp_.DecodePieces(pieces2))
        self.assertEqual(text, self.jasp_.DecodeIds(ids))

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestSentencepieceProcessor))
  return suite

if __name__ == '__main__':
    unittest.main()
