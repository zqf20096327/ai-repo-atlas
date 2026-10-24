# Freim32/vllmops

⭐ 100 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/Freim32/vllmops) · 个人维护

**自托管 vLLM 服务器的轻量控制平面：YAML 声明模型，CLI/TUI 管理全生命周期**

面向在裸机上运行 vLLM 的开发者：每个模型一个 YAML 文件，profile 分组管理，通过 CLI 或 Textual TUI 执行 start/stop/restart/status/health/logs 等生命周期命令，支持并行操作与幂等跳过。内置 LiteLLM 网关生成器 vllmops proxy，将所有运行中模型聚合到单一 OpenAI 兼容 URL 后并随启停自动同步。指标通过直接抓取 /metrics 存入内存环形缓冲，无需 Docker/Prometheus/Grafana。每项目用 uv 独立 venv 固定 vLLM 版本。要求 Linux/macOS 上的 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每模型一个 Git 友好的 YAML，profile 批量并行管理生命周期
- vllmops proxy 生成 LiteLLM 网关配置，单一 OpenAI 兼容 URL 聚合所有模型
- 直连 /metrics 抓取加内存环形缓冲，无需 Prometheus/Docker
- 每项目独立 venv 固定 vLLM 版本，mypy strict 与 380+ 测试

## 适用场景

- 在单机上声明式管理多个本地 vLLM 模型服务的启停与配置
- 把多个本地模型聚合到一个 OpenAI 兼容网关地址供客户端调用
- 在终端里实时查看各模型的指标与日志（TUI）

## 场景标签

`推理引擎` `模型网关` `MLOps` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A tiny control plane for bare-metal vLLM servers.
> L18: Self-hosted vLLM made simple. Declare each model in its own YAML file, group models into profiles in your project c

## 星数曲线

```mermaid
xychart-beta
    title "Freim32/vllmops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 98 --> 101
    line [99, 100, 100]
```

2026-10-18 99 → 2026-10-24 100（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b79b3dabc334` · [字段定义](../../DATASET.md)*
