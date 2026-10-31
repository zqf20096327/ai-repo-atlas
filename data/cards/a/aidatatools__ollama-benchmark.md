# aidatatools/ollama-benchmark

⭐ 397 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/aidatatools/ollama-benchmark) · [官网](https://llm.aidatatools.com/) · 个人维护

**通过 Ollama 测量本地 LLM 吞吐量的跨平台 CLI 工具**

面向本地大模型用户的 Python 命令行基准测试工具：依赖已安装的 Ollama，按机器内存大小自动检测并拉取相应规模的模型（如 4-7GB 用 gemma:2b，7-15GB 用 mistral:7b 等），逐个运行并报告 tokens-per-second 吞吐结果。支持 pip/pipx/uv 安装，Python 3.10 及以上测试通过，适用于 Windows/Linux/macOS。可自定义 YAML 基准模型清单，可指定自编译的 ollama 可执行文件路径，也可选择不发送系统信息与结果到远程服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 RAM 大小自动检测并拉取对应规模的基准模型
- 输出 tokens-per-second 吞吐结果
- 支持自定义 YAML 基准模型清单与自编译 ollama 路径
- 提供 --no-sendinfo 选项禁止发送系统信息与结果到远程服务器

## 适用场景

- 我在换硬件或调配置前先跑一遍基准，看本地模型实际生成速度
- 对比同一台机器上不同模型的 tokens-per-second 表现
- 给一批自定义模型清单做统一的吞吐测试

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: LLM Benchmark for Throughput via Ollama (Local LLMs)
> L5: Measure how fast your local LLMs _really_ are—with a simple, cross-platform CLI tool that tells you the tokens-per-s
> L9: Working Ollama installation.

## 星数曲线

```mermaid
xychart-beta
    title "aidatatools/ollama-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 396 --> 398
    line [397, 397]
```

2026-10-18 397 → 2026-10-31 397（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `692bdc6cadf1` · [字段定义](../../DATASET.md)*
