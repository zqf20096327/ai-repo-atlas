# AI4CharityPL/kancelaria-lex

⭐ 59 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/AI4CharityPL/kancelaria-lex) · 个人维护

**波兰律师的全本地法律案卷问答系统：回答逐句精确引用**

面向波兰律师的本地化法律案卷分析系统，界面为波兰语。加载 PDF/DOCX/TXT/RTF 案卷后，用波兰语提问，回答的每个句子都指向案卷中的精确字符位置，点击引用即打开原文高亮。机制上模型不直接写引文，只选句子编号、由代码重建文本，使编造引用无法表达；OCR（Tesseract 波兰语包）为可选手动开启且带永久标记。全程离线：非回环模型地址会阻止启动，四个 Docker 网段三个 internal。测量基于 722 文档、100 对问题，引用不一致为 0，引用准确率与正确拒答均高于 80%。不提供法律意见，仅供事实提取。QUICKSTART 面向无命令行经验用户，约 30 分钟安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型只选句子编号、代码重建引文，编造引用在结构上无法表达
- 全本地运行：非回环地址阻止启动，Docker 网段隔离，断网可运行
- OCR 可选且带永久 z OCR 标记与原文核对警告；不良提取会明确拒收
- 确定性程序期限计算器（代码计算而非模型）、哈希链审计日志、本地账户与 TOTP

## 适用场景

- 波兰律师在本地分析案卷并核验每句话的出处
- 需要向客户或审计方演示数据不出本机的合规场景
- GDPR/职业保密约束下处理敏感法律文件

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L85: You load the case file. You ask a question in plain Polish. You get an answer
> L87: from, down to the character.**

## 星数曲线

```mermaid
xychart-beta
    title "AI4CharityPL/kancelaria-lex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-31 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `24b9c04e8ab9` · [字段定义](../../DATASET.md)*
