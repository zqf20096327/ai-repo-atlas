# itsbroken-ai/RAGdrag

⭐ 42 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/itsbroken-ai/RAGdrag) · [官网](https://itsbroken.ai/ragdrag) · 个人维护

**RAG 流水线安全测试工具：6 阶段 27 类攻击技法评估**

面向授权测试的 RAG 管道安全评估 CLI：通过指纹识别、检索探测、知识泄露、投毒、劫持、规避六个阶段（R1–R6）发送请求并生成 schema 1.0 的 JSON 报告。证据分 validated/observed/inferred 三级，写操作（R4/R5）强制要求显式授权、清理 URL 与基线控制；默认 100 请求安全预算。可执行引擎注册表含 20 个技法 ID，27 条分类中其余为编目未实现条目。可选本地实验室提供靶机。Python 3.10+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- R1–R6 六阶段评估命令（fingerprint/probe/exfiltrate/poison/hijack/evade）
- 三级证据状态（validated/observed/inferred），validated 仅由标记回显产生
- R4/R5 写操作需显式授权、清理 URL 与三项已建立控制
- 本地捕获监听器默认 127.0.0.1，原始存储为敏感 opt-in

## 适用场景

- 对我方 RAG 系统做授权安全评估与知识泄露检测
- 验证投毒/劫持文档是否真的被检索到
- 审计 RAG 系统的向量数据库指纹与知识库边界

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: RAG pipeline security assessment toolkit for authorized testing.
> L9: RAGdrag assesses retrieval, generation, and ingestion boundaries through six
> L10: phases. The executable engine registry currently exposes 20 technique IDs. The

## 星数曲线

```mermaid
xychart-beta
    title "itsbroken-ai/RAGdrag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `67f42b041fca` · [字段定义](../../DATASET.md)*
