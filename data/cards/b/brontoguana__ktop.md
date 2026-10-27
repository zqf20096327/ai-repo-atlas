# brontoguana/ktop

⭐ 93 · Rust · 推送 2026-05-06 · [GitHub](https://github.com/brontoguana/ktop) · 个人维护

**面向混合 LLM 工作负载的终端系统资源监控器**

Rust 编写的 TUI 系统资源监控器，定位为跟踪混合 LLM 工作负载时的资源占用。读取 /proc 与 sysfs，提供 GPU（NVIDIA/AMD）、CPU、内存、网络、温度监控，OOM kill 追踪，进程表，50 个配色主题。单静态二进制，无运行时依赖，一行脚本安装到 /usr/local/bin，支持自更新与 cargo 源码构建。仅支持 Linux，GPU 监控为可选项，另有远程终端兼容模式与终端诊断命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPU/CPU/内存/网络/温度监控与 OOM kill 追踪（近 8 小时）
- Rust 单静态二进制，无运行时依赖，一行安装与自更新
- 50 个配色主题与 truecolor/Basic 颜色模式切换
- 远程终端兼容模式与终端闪烁诊断命令

## 适用场景

- 运行本地 LLM 推理时观察 GPU 显存与利用率
- 排查 OOM kill 与进程内存占用
- 通过 SSH 在远程终端监控系统资源

## 场景标签

 · 领域:系统监控/开发者工具

## 证据(README 行号)

> L5: A terminal-based system resource monitor built for tracking resource usage when running hybrid LLM workloads.
> L19: - **GPU Monitoring** — Per-GPU utilization and memory usage with color-coded sparkline history (NVIDIA + AMD)

## 星数曲线

```mermaid
xychart-beta
    title "brontoguana/ktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 91 --> 94
    line [92, 93, 93]
```

2026-10-18 92 → 2026-10-27 93（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `2046aba59b48` · [字段定义](../../DATASET.md)*
