# Srivatsa03/rag-redteam

⭐ 29 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/Srivatsa03/rag-redteam) · [官网](https://pypi.org/project/rag-redteam/) · 个人维护

**面向开发者的 RAG 管线红队安全测试工具，在 CI 中运行**

以 CLI 或 GitHub Action 形式对 RAG 管线整体做安全攻击测试：将用户 RAG 封装为三个方法（answer/add_documents/reset）或指向 HTTP 端点，注入七种攻击探针（间接提示注入、上下文泄漏、跨文档注入、工具调用注入、系统提示提取、引用完整性、嵌入反演），用金丝雀标记做确定性检测，无需 LLM 裁判。每项发现报告攻击成功率与 95% 置信区间，并映射 OWASP LLM/Agentic 与 MITRE ATLAS 编号，附修复指引；另提供 Defended 参考缓解层用于验证修复效果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七种攻击探针覆盖提示注入、来源泄漏与跨文档走私
- 金丝雀标记确定性检测，无需 LLM 裁判
- 每项发现附攻击成功率、95% 置信区间与 OWASP/MITRE ATLAS 映射
- 自带 Defended 参考缓解层，同一探针可量化修复效果

## 适用场景

- 在 CI 中对自有 RAG 管线做提示注入与数据泄漏红队测试
- 安全团队按 OWASP/ATLAS 框架跟踪 RAG 攻击面发现
- 更换模型或检索框架后重新测量注入防护效果

## 场景标签

`网络安全` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: Wrap your RAG in three methods, run rag-redteam, and it flags each finding with its rate, a confidence interval, an
> L21: `rag-redteam` tests the pipeline as a whole, and runs as a CLI or a GitHub Action.

## 星数曲线

```mermaid
xychart-beta
    title "Srivatsa03/rag-redteam 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-28 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c24a70095b4e` · [字段定义](../../DATASET.md)*
