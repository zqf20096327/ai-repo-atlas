# EriconYu/stocksniper

⭐ 38 · JavaScript · GPL-3.0 · 推送 2026-08-16 · [GitHub](https://github.com/EriconYu/stocksniper) · 个人维护 · 中文 README

**A股量化研究平台的开源展示壳（演示数据，FastAPI）**

Python 3 + FastAPI 编写的量化研究产品展示版：提供研究总览、市场环境、今日观察、策略中心、综合评分、回测入口、板块、信号、数据管理与执行日志等界面模块，前端为纯 HTML/CSS/JS 无需 Node 构建，不依赖数据库与行情账号即可本地运行。所有行情、评分与信号均为固定演示数据；不含生产级采集器、私有策略算法、回测引擎与调度，受限能力统一跳转到付费完整版。GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 10 个量化研究工作流模块的可运行产品壳
- 无数据库、无行情账号、无 API key 的本地体验
- 后端仅依赖 FastAPI 与 Uvicorn，前端无需 Node 构建
- 提供 Docker Compose 与 OpenAPI 文档

## 适用场景

- 本地体验 A 股量化研究平台的界面与信息架构
- 在展示壳基础上扩展自己的 FastAPI 量化研究功能
- 了解完整版产品的功能边界后联系作者获取商业版

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: A **Python 3 open-source showcase** for an A-share quantitative research platform. The project provides a runnable p
> L7: > This repository is a community showcase. It does not include production market-data collectors, private data provi
> L13: StockSniper started as a Go-based stock crawler. Community Edition 2.0 has been completely rebuilt with Python 3 an

## 星数曲线

```mermaid
xychart-beta
    title "EriconYu/stocksniper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `a6d6949160d8` · [字段定义](../../DATASET.md)*
