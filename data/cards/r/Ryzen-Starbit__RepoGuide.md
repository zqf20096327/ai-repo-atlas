# Ryzen-Starbit/RepoGuide

⭐ 11 · Python · 推送 2026-11-09 · [GitHub](https://github.com/Ryzen-Starbit/RepoGuide) · 个人维护

**让开发者用自然语言提问来理解陌生代码仓库的 RAG 工具**

RepoGuide 读取 GitHub 仓库，用 Sentence Transformers 生成嵌入并经 FAISS 向量检索，支持对代码提问、复杂度估算、复杂文件风险检测、依赖与变更影响分析及代码解释。前端为 Streamlit，后端为 FastAPI/Uvicorn，通过 git clone 克隆仓库后以 uvicorn 与 streamlit 两条命令分别启动后端和前端，在浏览器中使用。README 未列出可执行安装包，也未声明硬件要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载 GitHub 仓库后用自然语言提问代码问题
- Sentence Transformers 嵌入 + FAISS 向量检索
- 代码复杂度估算与复杂文件风险检测
- 依赖关系与变更影响分析

## 适用场景

- 接手陌生代码库时快速了解项目结构
- 为缺少文档的项目生成代码解释
- 评估修改某文件对依赖模块的影响

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: RepoGuide is an intelligent repository exploration tool that helps developers quickly understand unfamiliar codebase
> L56:  - Sentence Transformers
> L57:  - FAISS vector search

## 星数曲线

```mermaid
xychart-beta
    title "Ryzen-Starbit/RepoGuide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-11-11", "2026-11-18"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-10-18 10 → 2026-11-18 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `37316f437d16` · [字段定义](../../DATASET.md)*
