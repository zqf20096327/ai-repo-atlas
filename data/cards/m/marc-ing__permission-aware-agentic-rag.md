# marc-ing/permission-aware-agentic-rag

⭐ 19 · Python · MIT · 推送 2026-08-30 · [GitHub](https://github.com/marc-ing/permission-aware-agentic-rag) · 个人维护 · 中文 README

**面向企业共享文档的权限感知 Agentic RAG 参考实现**

企业知识库问答系统参考实现：目录级 ACL 贯穿知识路由、混合检索（Qdrant Dense/Sparse + RRF）、Rerank、LLM Evidence 与 Citation 链路，权限由确定性后端逻辑判断，Agent 与大模型不参与授权决策。支持 Markdown/PDF/DOCX/DOC 入库与中英文 OCR，答案基于授权 Evidence 生成并支持行号/页码定位；撤权后下次检索即时失效。技术栈为 Python 3.12+/FastAPI/MySQL/MinIO/Qdrant，经 uv 与 Docker Compose 部署。授权粒度为目录级，未实现 SSO 与多租户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 目录级 ACL 贯穿检索/路由/Citation 全链路，权限由后端确定性判断
- Qdrant Dense/Sparse 混合检索 + RRF 融合 + 可接入外部 Rerank Provider
- 撤权或文档变更后下一次检索与 Citation 访问即时按新权限判定
- 多格式入库含图片提取、扫描页判定与中英文 OCR

## 适用场景

- 企业内不同权限用户通过同一知识库入口进行安全问答
- 对共享文档库做带引用定位（Markdown 行号/PDF 页码）的问答
- 验证撤权后旧引用即时失效的权限审计场景

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: 一个面向企业共享文档的权限感知型 Agentic RAG 参考实现。系统将目录 ACL 贯穿到知识路由、混合检索、Rerank、LLM Evidence 和 Citation 访问链路，让不同用户可以通过同一个知识库入口安全问答。
> L14: - 可追溯问答：基于授权 Evidence 生成答案，Citation 支持 Markdown 行号定位和 PDF 页码跳转。

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/permission-aware-agentic-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d233f8c79263` · [字段定义](../../DATASET.md)*
