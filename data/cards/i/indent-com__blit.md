# indent-com/blit

⭐ 21 · Rust · MIT · 推送 2026-10-26 · [GitHub](https://github.com/indent-com/blit) · [官网](https://blit.sh) · 组织维护

**面向浏览器与 AI agent 的终端复用器和实验性 Wayland 合成器**

blit 在服务器端托管 PTY 并追踪完整解析后的终端状态，将增量（LZ4 压缩）经 WebSocket/WebRTC 推送到浏览器，用 WebGL 渲染；提供终端的编程控制接口（start/show/send/output）、进程执行、端口转发、SOCKS5 代理与客户端管理。Linux 上每个终端附带实验性无头 Wayland 合成器，可捕获 GUI 窗口为 H.264/AV1 视频流并支持点击/输入注入。同时发布供计算机 agent 使用的技能。安装经 curl 脚本或 PowerShell，Docker 提供演示镜像；客户端控制无权限分离是已知限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PTY 托管 + 二进制差分增量推送，浏览器 WebGL 渲染终端
- 实验性无头 Wayland 合成器：GUI 窗口捕获为 H.264/AV1 视频流，支持 surface click/type 注入
- 端口转发（含 UDP）、SOCKS5 代理与命名远程管理
- 提供 @blit-sh/react 与 @blit-sh/solid 框架绑定及 computer agent skill

## 适用场景

- 在浏览器中访问远程或本地的终端与 GUI 程序
- 让 AI agent 通过编程接口操作终端与图形界面
- 通过 blit share 以 URL 分享终端会话（WebRTC）
- 把远程服务器端口/SOCKS 代理转发到本地

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Terminal multiplexer and experimental Wayland compositor for browsers and AI agents. Nothing to configure, no requir
> L5: We publish a computer agent skill.

## 星数曲线

```mermaid
xychart-beta
    title "indent-com/blit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `fe04526ae5fe` · [字段定义](../../DATASET.md)*
