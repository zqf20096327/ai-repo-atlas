# microsoft/Planetary-Explorer

⭐ 200 · Python · MIT · 推送 2026-09-10 · [GitHub](https://github.com/microsoft/Planetary-Explorer) · 组织维护

**微软的AI地理空间应用：用自然语言探索地球科学数据**

基于 Azure AI Foundry / Microsoft Agent Framework 构建的地理空间生成式 AI 应用：多 agent 系统将自然语言问题转为地理空间答案，把 Microsoft Planetary Computer 的 130+ STAC 收藏、Fabric Lakehouse、Azure AI Search 文档与天气/地理空间模型（GPT、Aurora、NVIDIA Earth-2 FCN、MAI Weather）聚合到同一对话界面。前端为 React 地图+聊天应用，另提供 Teams bot、M365 Copilot 声明式 agent 与 MCP server。通过 Bicep + GitHub Actions 自动部署到 Azure，声明为可复用模式而非受支持的微软产品。

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

- 多 agent 架构将自然语言问题转为地图渲染与推理结果
- 融合 MPC STAC 收藏、Fabric Lakehouse、Azure AI Search 与多天气模型（3 模型 ensemble 预报）
- GEOINT 模块：视觉、地形、机动性、对比、建筑损毁分析
- 所有 agent 可经 MCP server 暴露给 VS Code / Claude Desktop

## 适用场景

- 用自然语言检索与可视化卫星影像和地表数据
- 干旱、洪水、火灾等自然灾害的监测与风险分析
- 候选选址评分与设施韧性持续监控
- 通过 Teams 或 M365 Copilot 在日常工作界面中查询地理空间数据

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L6: Planetary Explorer, built on AI Foundry, demonstrates how organizations can use Microsoft Planetary Computer Pro to 
> L10: Planetary Explorer turns natural-language questions into grounded geospatial answers. Its multi-agent system picks 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Planetary-Explorer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 198 --> 201
    line [199, 200, 200]
```

2026-10-18 199 → 2026-10-25 200（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `2ea116c8d42f` · [字段定义](../../DATASET.md)*
