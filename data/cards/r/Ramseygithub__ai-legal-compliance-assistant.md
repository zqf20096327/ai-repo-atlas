# Ramseygithub/ai-legal-compliance-assistant

⭐ 336 · Python · 推送 2026-02-03 · [GitHub](https://github.com/Ramseygithub/ai-legal-compliance-assistant) · [官网](http://0.0.0.0:8000/) · 个人维护 · 中文 README

**面向法规解读的 AI 合规分析平台：RAG+知识图谱问答**

基于 FastAPI 的法律合规分析系统，接入阿里云百炼 AI 服务（Qwen-Turbo 生成回答、text-embedding-v1 向量化），面向酒类饮品定价等法规场景。功能包括 PDF/HTML 法规文档摄取与分段、向量索引语义检索、法律实体与关系抽取生成 JSON 知识图谱、RAG 增强问答、多因素合规判定与风险评级，前端提供文档管理、实时问答与合规报告界面。数据以 JSON 文件与本地文件系统存储，当前仅支持 PDF/HTML 格式，依赖网络访问阿里云服务。

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

- PDF/HTML 法规文档摄取、元数据抽取与向量索引
- 法律实体/关系抽取生成 JSON 知识图谱
- RAG+知识图谱增强的 Qwen-Turbo 问答
- 多因素合规判定、风险评级与违规识别

## 适用场景

- 上传法规文档后进行合规问答与解释
- 对业务行为做多因素合规判定并获取风险评级
- 查询法规条文、处罚等实体构成的知识图谱

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: > An **AI-based legal compliance analysis platform** integrating **Alibaba Cloud Bailian** AI capabilities for regul
> L29: - 💬 Generates professional answers via **Qwen-Turbo model**

## 星数曲线

```mermaid
xychart-beta
    title "Ramseygithub/ai-legal-compliance-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 335 --> 337
    line [336, 336]
```

2026-10-18 336 → 2026-10-29 336（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `970b41a45943` · [字段定义](../../DATASET.md)*
