# MuhammadUsmanGM/code-stick

⭐ 63 · TypeScript · NOASSERTION · 推送 2026-05-21 · [GitHub](https://github.com/MuhammadUsmanGM/code-stick) · [官网](https://www.npmjs.com/package/code-stick) · 个人维护

**装进 USB 的离线 AI 编程代理：即插即用零安装**

将 opencode（终端编程代理）与 Ollama（本地模型运行时）打包到 USB 上，预构建 Windows x64/ARM64、macOS Apple Silicon/Intel、Linux x64/ARM64 六个目标平台。插入支持机器后双击启动脚本，代理通过 127.0.0.1:11434 访问 USB 上的 Ollama，退出即终止进程，主机无残留。默认推荐 Qwen2.5-Coder 7B（8 GB 内存可跑，占 32 GB 盘），限制包括 USB 3.0 以上才宜跑大于 7B 模型、macOS 启动器未公证、大模型首句延迟 30–90 秒。面向需要在受限/离线/他人设备上使用本地编程代理的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六个平台目标预构建，目标机器零安装
- opencode + Ollama 全程从 USB 运行，主机无残留
- 内置模型目录（Qwen2.5-Coder 7B/14B/32B、Phi-3 Mini）与 add/remove-model 管理
- 提供 install/start/doctor/prune 等十余个子命令

## 适用场景

- 在银行、医院、实验室等离线或受限机器上使用 AI 编程代理
- 在共享或借用笔记本上随身携带本地编程助手且不留痕
- 处理 NDA 或闭源项目时避免代码上云
- 飞行/通勤等弱网环境下继续用代理写代码

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: > **Plug in a USB. Get an offline AI coding agent on any laptop.**
> L27: Under the hood it's opencode (terminal coding agent) talking to Ollama (local model runner), both pre-built for eve
> L101: - **Install machine:** Node 20+. Target machines need **nothing**.

## 星数曲线

```mermaid
xychart-beta
    title "MuhammadUsmanGM/code-stick 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-28 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7992d9ba8d1c` · [字段定义](../../DATASET.md)*
