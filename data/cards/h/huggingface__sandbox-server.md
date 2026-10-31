# huggingface/sandbox-server

⭐ 14 · Rust · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/huggingface/sandbox-server) · 组织维护

**Hugging Face Jobs 沙箱内运行的静态代理服务器：命令执行、文件传输、端口转发**

以约 671KB 的 x86_64 musl 静态二进制运行于任意含 /bin/sh 的 Docker 镜像内，作为 hf sandbox / huggingface_hub.Sandbox 客户端的沙箱端组件，经 Jobs 代理通信。提供专用模式（一作业一沙箱，完整 VM 隔离）与宿主模式（单作业承载多沙箱，每沙箱独立 uid、私有 home 与 Landlock LSM 规则集，毫秒级创建）。功能含命令执行与 NDJSON 流式输出、后台进程管理、文件读写 API、keepalive 与空闲看门狗。认证采用 SBX_TOKEN 与每沙箱 256 位能力令牌；宿主模式有已知隔离缺口（无聚合资源配额、共享出站 TCP 等），Rust 编写，需 cargo 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单静态二进制（约 671KB，musl，零运行时依赖）
- 专用/宿主双模式：宿主模式以 uid + Landlock 实现单 VM 内多沙箱隔离
- 命令执行 NDJSON 流式输出、文件分段并行传输、端口代理
- 空闲看门狗自动退出以停止计费

## 适用场景

- 为 AI agent 或不可信代码提供隔离的云上命令执行环境
- 在一个作业内运行多个轻量隔离沙箱（SandboxPool）
- 通过 HTTP API 在沙箱中执行命令、传文件、转发端口

## 场景标签

 · 领域:云基础设施/代码沙箱

## 证据(README 行号)

> L3: The in-sandbox agent powering `hf sandbox` / `huggingface_hub.Sandbox` — isolated cloud
> L6: A single static binary (~671KB, x86_64 musl, zero runtime dependencies) that runs in **any**

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/sandbox-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6ebdd62edca6` · [字段定义](../../DATASET.md)*
