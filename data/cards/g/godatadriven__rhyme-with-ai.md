# godatadriven/rhyme-with-ai

⭐ 46 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/godatadriven/rhyme-with-ai) · 组织维护

**用 BERT 模型生成押韵词的 Streamlit 网页应用**

基于 Streamlit 的网页应用：用户输入单词或短语，应用使用 HuggingFace transformers 的 BERT 类模型生成押韵候选词，本地运行需通过 conda 环境安装依赖、pip 安装包并下载模型权重，支持 make streamlit 启动、Docker 构建与部署到 Google App Engine。README 仅含本地开发与部署说明，功能描述细节有限，Todo 项显示部分功能（TokenWeighter 集成）尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 transformers BERT 模型生成押韵词
- 提供 Streamlit 网页界面
- 支持 Docker 构建运行与 Google App Engine 部署

## 适用场景

- 写歌词或文案时查找押韵词
- 体验 BERT 模型的词语生成能力

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L16: Download the weights of the models (if you get any errors, make sure these align with those specified in `app/app.p
> L25: make streamlit

## 星数曲线

```mermaid
xychart-beta
    title "godatadriven/rhyme-with-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-30 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `6fbd9290d38e` · [字段定义](../../DATASET.md)*
