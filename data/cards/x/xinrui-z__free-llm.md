# xinrui-z/free-llm

⭐ 26 · Astro · MIT · 推送 2026-05-20 · [GitHub](https://github.com/xinrui-z/free-llm) · [官网](https://free-llm-apis.pages.dev/) · 个人维护 · 中文 README

**免费 LLM API 提供商的实时状态监控仪表盘与清单**

聚合免费 LLM API 提供商的监控站点：Cloudflare Worker 每小时对各提供商做健康检查并写入 KV，站点展示实时状态、响应延迟、RPM/RPD 限额、模型列表与 90 天可用性热力图，并自动记录宕机、恢复与模型变更的变更日志。所有收录提供商均为 OpenAI 兼容的 /v1/chat/completions 格式，且须有永久免费层。站点可导出 LiteLLM、Cursor、LobeChat、Open WebUI 的配置文件。前端为 Astro，自托管依托 Cloudflare 免费层；健康检查 Worker 本身不包含在仓库中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cloudflare Workers 每小时健康检查 + 90 天可用性热力图
- 自动生成宕机/恢复/模型变更日志
- 导出 LiteLLM / Cursor / LobeChat / Open WebUI 可用配置
- 收录标准要求永久免费层且 OpenAI 兼容

## 适用场景

- 挑选当前可用的免费 LLM API 提供商
- 查看某提供商的限速、模型与历史可用性
- 获取可直接导入常用 LLM 工具的配置文件

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: Real-time status monitoring for free LLM API providers — live status, latency, rate limits, and 90-day uptime histor
> L15: Each provider page shows current status, response latency, RPM / RPD limits, model list, and a 90-day uptime heatma
> L33: - **OpenAI-compatible** — all listed providers use the `/v1/chat/completions` format

## 星数曲线

```mermaid
xychart-beta
    title "xinrui-z/free-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6536fce0afb0` · [字段定义](../../DATASET.md)*
