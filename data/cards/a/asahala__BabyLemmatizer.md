# asahala/BabyLemmatizer

⭐ 17 · Python · 推送 2026-08-13 · [GitHub](https://github.com/asahala/BabyLemmatizer) · 个人维护

**面向楔形文字等古语言的神经词形还原与词性标注工具**

基于 OpenNMT-py 的神经序列到序列模型，对转写后的阿卡德语、苏美尔语、乌拉尔图语、古希腊语、拉丁语等古语言文本做词性标注与词形还原（lemmatization），并提供基于词典的统计后处理修正。提供多种预训练模型，通过命令行读取 CoNLL-U 文件进行标注、训练、评估与 n 折交叉验证，默认在 GPU 上运行，也可加 --use-cpu 参数。要求 Python 3.9 与 OpenNMT-py 3.2.0（其他版本可能导致崩溃），需手动编辑 preferences.py 配置路径。附有 2023 年 RANLP 古语言处理工作坊论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 POS 标注与词形还原作为机器翻译（seq2seq）任务处理
- 提供苏美尔语、亚述语、巴比伦语、乌拉尔图语等预训练模型
- 支持从 CoNLL-U 数据构建、训练、评估与 n 折交叉验证
- 结合词典式后处理对标注结果做统计修正与可靠性评分

## 适用场景

- 对转写的阿卡德语语料做词形还原与词性标注
- 为古语言语料构建可检索文本或词嵌入
- 在自己的 CoNLL-U 数据上训练与交叉验证古语言标注模型

## 场景标签

 · 领域:计算语言学/NLP

## 证据(README 行号)

> L4: State-of-the-art neural part-of-speech-tagger and lemmatizer finetuned for Cuneiform languages such as Akkadian, Sum
> L9: BabyLemmatizer approaches POS-tagging and lemmatization as a Machine Translation (i.e. a sequence-to-sequence) task.

## 星数曲线

```mermaid
xychart-beta
    title "asahala/BabyLemmatizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `9bd4346356ba` · [字段定义](../../DATASET.md)*
