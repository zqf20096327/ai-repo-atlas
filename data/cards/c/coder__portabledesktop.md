# coder/portabledesktop

⭐ 32 · Go · MIT · 推送 2026-09-08 · [GitHub](https://github.com/coder/portabledesktop) · 组织维护

**为 AI agent 提供可控真实 Linux 桌面的 Go 单二进制**

单文件 Go 二进制，内嵌压缩的 Linux 运行时，首次运行时解包并直接管理桌面会话：提供真实 GUI 应用、鼠标/键盘输入、截图与录制，无需配置容器或显示服务器。`up --json` 输出显示号、VNC 端口等会话元数据供 agent 工具程序化接入；内置 noVNC 人类观察/干预浏览器（默认 6080 端口）。支持 Linux x64 与 arm64。VNC 端点默认无认证，需仅在可信边界暴露。示例含 Anthropic/OpenAI 驱动的 agent 与 Docker agent 循环。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制内嵌 Linux 运行时，首运行解包，无需容器或显示服务器
- `up --json` 输出 VNC 端口/环境变量等会话元数据供程序化接入
- noVNC 浏览器端人类观察与干预（human-in-the-loop）
- 提供截图、录制与鼠标/键盘输入控制

## 适用场景

- 为 computer-use 类 AI agent 提供可操作的真实桌面环境
- 调试 agent 运行过程并在其卡住时人工介入
- 在无容器/无显示服务器配置的环境快速起一个桌面会话

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Run a real Linux desktop for AI agents.
> L7: your agent a controllable desktop with real GUI apps, mouse/keyboard input,
> L24: `up --json` prints session metadata (display number, VNC port, environment

## 星数曲线

```mermaid
xychart-beta
    title "coder/portabledesktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e690fd1154a8` · [字段定义](../../DATASET.md)*
