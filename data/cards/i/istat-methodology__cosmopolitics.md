# istat-methodology/cosmopolitics

⭐ 15 · Python · 推送 2026-01-15 · [GitHub](https://github.com/istat-methodology/cosmopolitics) · 组织维护

**国际贸易分析仪表盘：疫情冲击与流动性政策的可视化与预测**

Istat 团队为欧洲统计局 2021 Big Data Hackathon 开发的开源仪表盘，基于 Vue.js 与 Docker 微服务架构，分析工具链集成 Python 与 R。提供五类功能：交互式地图展示欧盟成员国宏观经济与进出口指标、基于 Google 流动性数据的政策限制指标、COVID-19 对贸易的影响评估（含中断时间序列分析与 nowcasting/forecasting）、基于 COMEXT 运输方式数据的贸易关系图分析，以及按产品类别的进出口份额分解。数据来源为 COMEXT、Eurostat 与 Google Mobility。克隆仓库后 docker-compose up 即可在浏览器访问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互式地图：欧盟 27 国进出口与宏观经济指标
- COVID-19 贸易影响评估：中断时间序列分析，支持 nowcast 与自定义情景 forecast
- 基于 COMEXT 运输数据的国际贸易关系图分析与网络度量
- Google 流动性数据生成 0–1 范围的政府限制政策指标

## 适用场景

- 分析疫情前后两国间进出口的月度变化
- 模拟不同流动性限制情景下的贸易预测
- 查看成员国按产品类别的进出口结构变化

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Cosmopolitics is an open source dashboard implemented using modern javascript frameworks (Vue.js) and microservice a
> L21: situation between the two countries in the period before and after a specific reference date (suggested by the user

## 星数曲线

```mermaid
xychart-beta
    title "istat-methodology/cosmopolitics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `dd4243ad6167` · [字段定义](../../DATASET.md)*
