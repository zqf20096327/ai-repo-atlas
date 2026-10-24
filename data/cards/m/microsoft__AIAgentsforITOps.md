# microsoft/AIAgentsforITOps

⭐ 85 · PowerShell · MIT · 推送 2026-09-22 · [GitHub](https://github.com/microsoft/AIAgentsforITOps) · 组织维护

**面向 IT/Ops 的 Azure AI agent 基础设施管理工作坊**

微软提供的培训仓库，教学重点为在 Azure 上管理 AI agent 的基础设施而非 agent 开发。提供两条自包含路径：路径 1 在 AKS 上自托管 agent 并调用 Microsoft Foundry 模型（gpt-5.4-mini，OpenAI 兼容 Responses API，代码内自实现 RAG）；路径 2 由 Foundry 托管 agent 与知识库，AKS 仅承载 Web UI。内容覆盖托管标识与 RBAC、VNet 隔离、Key Vault 密钥管理、Application Insights 监控与成本管理，两条路径均部署同一会议专家问答示例 agent，并附月度成本估算（约 167-177 美元+用量）。

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

- 两条自包含工作坊路径：AKS 自托管与 Foundry 托管
- 覆盖托管标识/RBAC、私有网络、Key Vault、监控与成本管理
- 同一会议专家问答示例 agent，Web 聊天界面与 RAG 检索会议数据
- 附各路径 Azure 资源月度成本估算

## 适用场景

- IT/Ops 团队学习在 Azure 上部署与管理 AI agent 的基础设施
- 对比 AKS 自托管与 Foundry 托管两种 agent 托管方式
- 练习 Azure 服务间的安全接入、监控与成本控制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This workshop teaches developers and IT/Ops professionals how to manage AI agents on Azure infrastructure. The focus
> L19: This workshop offers **two distinct paths** for managing AI agents on Azure. Both paths use the same conference exp

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/AIAgentsforITOps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-24 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e3e9cc17d3b8` · [字段定义](../../DATASET.md)*
