# eli-labz/Third-Eye

⭐ 862 · TypeScript · MIT · 推送 2026-06-13 · [GitHub](https://github.com/eli-labz/Third-Eye) · [官网](https://geospatialcommand.center) · 个人维护

**开源 OSINT 全球情报聚合平台：多源态势感知仪表盘**

基于 Next.js 16 与 MapLibre GL 的自托管 OSINT 平台，将航空、海事、CCTV、地震、火灾、新闻、网络威胁、冲突区、加密货币追踪、制裁名单等 16 个实时数据层聚合到 WebGL 渲染的地图界面。内置 RECON 工具集（端口扫描、DNS、WHOIS、SSL、CVE、钱包追踪、OFAC 检索），核心层无需 API key。可选开启的 Smart System 模块（默认关闭）叠加人机协同的数据融合与咨询式 AI 模型（异常检测、摘要、风险评分），所有建议进入人工审批队列。提供 npm 源码运行、Docker Compose 与 GHCR 预构建镜像三种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个实时数据层聚合（航空/海事/CCTV/地震/新闻/制裁等）
- 内置 RECON 工具集：端口扫描、WHOIS、CVE、加密钱包追踪与 OFAC 交叉核验
- 核心层零 API key 即可用，Docker 单命令自托管
- 可选 Smart System：人机协同数据融合，含异常检测/摘要/风险评分，决策支持且全程审计

## 适用场景

- 在单一地图界面实时监控全球多源情报态势
- 对域名、IP、加密钱包做侦察与制裁名单核验
- 自托管部署用于情报分析或态势感知工作台

## 场景标签

`网络安全` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L171: ## 🧠 Smart System (optional, off by default)
> L174: An optional, **feature-flagged**, **human-in-the-loop** data-fusion module that
> L179: It is **decision-support only** — nothing autonomous, kinetic, or real-world. It

## 星数曲线

```mermaid
xychart-beta
    title "eli-labz/Third-Eye 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 876 --> 878
    line [877, 877]
```

2026-10-18 877 → 2026-10-22 877（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6833a117cccf` · [字段定义](../../DATASET.md)*
