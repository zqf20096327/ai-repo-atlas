# DivitMittal/DocAssist-LLM

⭐ 19 · Jupyter Notebook · MIT · 推送 2026-10-22 · [GitHub](https://github.com/DivitMittal/DocAssist-LLM) · [官网](https://deepwiki.com/DivitMittal/DocAssist-LLM) · 个人维护

**RAG 增强的 LLaMa 类 Transformer LLM，用于编程文档问答**

基于论文《DocAssist: Large Language Models' Brilliance in the Art of Web Development Dialogue》的项目：实现一个 LLaMa 类 Transformer 架构的 LLM（RMSNorm 预归一化、SwiGLU 激活、RoPE 旋转位置编码），并结合检索增强生成（RAG），从知识库中检索相关文档片段后生成针对编程语言/框架文档的回答。前端使用 Python 的 Streamlit 提供聊天界面。面向需要查阅和理解编程文档的开发者。README 未给出安装或运行命令，仓库含 Nix flake 相关 CI 徽章。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLaMa 类架构：RMSNorm 预归一化、SwiGLU 激活函数、RoPE 旋转位置编码
- RAG：先从知识库检索相关文档片段，再由生成模型合成回答
- Streamlit 聊天前端界面
- 含 LLaMA、Attention Is All You Need 等论文引用

## 适用场景

- 向文档知识库提问并获取相关片段支撑的回答
- 开发者查阅编程语言/框架文档的对话式助手

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: RAG-enhanced LLaMa-like transformer neural network based LLM for assistance on programming languages/frameworks' do
> L21: The RAG-LLTN model integrates Retrieval-Augmented Generation (RAG) capabilities with the architecture of LLaMa-like
> L43: A user-friendly interface is provided using Streamlit (Python).

## 星数曲线

```mermaid
xychart-beta
    title "DivitMittal/DocAssist-LLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d477b22a153e` · [字段定义](../../DATASET.md)*
