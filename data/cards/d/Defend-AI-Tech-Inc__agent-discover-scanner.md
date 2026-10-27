# Defend-AI-Tech-Inc/agent-discover-scanner

⭐ 22 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/Defend-AI-Tech-Inc/agent-discover-scanner) · [官网](https://defendai.ai/scanner) · 组织维护

**企业 AI Agent 资产清点与 GHOST 检测扫描器**

DefendAI 平台的开源组件，用于自动发现与清点企业内运行的自主 AI agent。通过五层检测（Python/JS 静态分析、psutil 实时网络观测、Kubernetes eBPF 事件、osquery 端点发现、云审计日志）交叉关联，将 agent 分类为 GHOST/CONFIRMED/UNKNOWN/SHADOW/ZOMBIE，并给出 SaaS 连接映射与风险评分。以 PyPI 包（agentdiscover）分发，可选上传结果至 DefendAI 商业平台；部分层需要 sudo、osquery 或集群权限。面向企业安全与 AgentOps 治理场景。

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

- 五层检测（静态分析/网络/K8s eBPF/端点/云审计）交叉关联为单一 agent 清单
- GHOST 分类：运行时存在 AI 调用但代码库无对应来源
- Bedrock 前向 DNS 缓存识别轮转 EC2 IP 的运行时端点
- 输出 SARIF/AIBOM/审计报告，支持 GitHub Security tab 集成

## 适用场景

- 盘点开发机上实际在运行的 AI agent 与组件
- 生成 AIBOM 合规审计包
- 发现无源码归属的 GHOST agent 与影子 AI 使用

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: *Part of the DefendAI platform for autonomous AI governance*
> L221: AgentDiscover Scanner runs **five detection layers** simultaneously and correlates them into a single agent invent
> L223: |Layer|Name|Technology|Requirements|

## 星数曲线

```mermaid
xychart-beta
    title "Defend-AI-Tech-Inc/agent-discover-scanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e650341b1666` · [字段定义](../../DATASET.md)*
