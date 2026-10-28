# aveloxis/aveloxis

⭐ 19 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/aveloxis/aveloxis) · [官网](https://aveloxis.io) · 组织维护

**开源社区健康分析平台：GitHub/GitLab 贡献者指标、SBOM 与漏洞扫描**

用 Go 编写的开源社区健康度量系统，由 CHAOSS 联合创始人发起，定位为 Augur 的后继项目。从 GitHub 和 GitLab 采集数据，提供 CHAOSS 指标、贡献者分析、SBOM 生成与漏洞扫描、许可证/版权扫描（ScanCode）。由 CLI、采集调度器、Web GUI（OAuth 登录、可视化、监控面板）与 REST API 组成，数据存于 PostgreSQL（163 张表，与 Augur schema 对齐），支持 Docker Compose/Podman 部署，兼容已有 Augur 数据库迁移。面向大规模仓库群（fleet）运维。

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

- GitHub/GitLab 双平台数据采集与 CHAOSS 指标计算
- SBOM 生成、漏洞扫描与 ScanCode 许可证/版权扫描
- 与 Augur schema 全对齐（163 张表），可复用现有 Augur 数据库与 API key
- Docker Compose/Podman 五容器部署（postgres/migrate/serve/web/api）

## 适用场景

- 度量开源项目的社区健康度与贡献者活动
- 为大型仓库群做供应链分析（SBOM、漏洞、许可证合规）
- 从 Augur 迁移并继续历史数据采集

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **Open source community health analytics at fleet scale — the Go successor to Augur, built by CHAOSS co-founders**, 
> L15: Read about the way Claude Code was used to create Aveloxis

## 星数曲线

```mermaid
xychart-beta
    title "aveloxis/aveloxis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `9b6806804fa6` · [字段定义](../../DATASET.md)*
