# pajitosingh/vllm-qwen-launcher

⭐ 13 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/pajitosingh/vllm-qwen-launcher) · 个人维护

**Qwen3.6 vLLM 启动脚本与优化聊天模板工具包**

面向本地部署 Qwen 3.6 27B（兼容 Qwen 3/3.5）的工具包，含两部分：vllm_launch.sh 启动脚本，封装 vllm serve，提供模型目录自动发现、量化类型识别（AWQ/GPTQ/FP8/Marlin）、交互式参数覆盖、残留进程清理、GPU 自动检测与非交互/试运行模式；以及一套在社区模板基础上合并改进的 Jinja2 聊天模板，处理思维块自愈、工具调用参数解析、前缀缓存复用、视觉内容渲染等。README 标注在双 24 GB GPU（RTX 3090/4090，共 48 GB）上测试，推荐 FP8 量化 + 张量并行配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- bash 启动脚本封装 vllm serve：模型自动发现、量化感知配置、残留进程清理、GPU 自动检测
- 合并多社区模板的 Jinja2 聊天模板：未闭合 <think> 自愈、JSON 字符串参数解包、确定性工具错误检测
- 支持按请求经 chat_template_kwargs 切换 enable_thinking，无需重启服务
- 附 VRAM 需求表：27B 模型各量化档位与双 24 GB GPU 适配方案

## 适用场景

- 在双 24 GB 显卡上以 FP8/AWQ/GPTQ 量化运行 Qwen 27B 级模型
- 替换 vLLM 默认聊天模板以改善工具调用与思维块处理
- 脚本化/交互式管理本地 vLLM 服务启动参数

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: A portable vLLM launch script and **significantly improved chat template** for
> L93: A battle-tested bash script that wraps `vllm serve` with:
> L109: - Python venv with `vllm` installed (tested with vLLM ≥ 0.6.0)

## 星数曲线

```mermaid
xychart-beta
    title "pajitosingh/vllm-qwen-launcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `20db35e8c0ba` · [字段定义](../../DATASET.md)*
