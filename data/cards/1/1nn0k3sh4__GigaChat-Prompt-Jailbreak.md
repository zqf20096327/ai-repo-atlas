# 1nn0k3sh4/GigaChat-Prompt-Jailbreak

⭐ 29 · MIT · 推送 2025-12-27 · [GitHub](https://github.com/1nn0k3sh4/GigaChat-Prompt-Jailbreak) · 个人维护

**GigaChat 内容过滤器绕过漏洞的技术研究报告**

针对 GigaChat LLM 的 AI 安全研究文档：作者通过“上下文伪装”技术（专业角色扮演 + 科技术语 + 教育语境）测试内容过滤器绕过，记录了漏洞类别（CWE-863/CWE-693）、CVSS 6.5 评分、模型响应中的科学错误分析以及修复建议（多层验证、专家核查、审计）。研究遵循负责任披露流程，已通过 SberAI 渠道提交报告；文档刻意省略可复现的具体提示词与危险内容细节。这是纯文档型仓库，不含可安装运行的软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别 GigaChat 内容过滤器绕过漏洞（GigaChat-CFB-2025-001，CVSS 6.5）
- “上下文伪装”攻击向量的技术描述与风险分析
- 模型响应科学准确性问题的原子平衡分析示例
- 多层验证与专家核查的修复建议及负责任披露流程记录

## 适用场景

- LLM 安全团队了解角色伪装类过滤器绕过漏洞
- AI 安全研究人员参考漏洞分析方法与披露流程
- 评估专业领域 LLM 内容过滤系统的改进方向

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: This research identifies a method to bypass safety systems in the GigaChat LLM, enabling the generation of potentia
> L96: **Identifier**: GigaChat-CFB-2025-001 (Content Filter Bypass)

## 星数曲线

```mermaid
xychart-beta
    title "1nn0k3sh4/GigaChat-Prompt-Jailbreak 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-28 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `702de17f45c2` · [字段定义](../../DATASET.md)*
