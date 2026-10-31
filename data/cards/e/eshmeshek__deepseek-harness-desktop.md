# eshmeshek/deepseek-harness-desktop

⭐ 14 · Rust · MIT · 推送 2026-09-15 · [GitHub](https://github.com/eshmeshek/deepseek-harness-desktop) · 个人维护

**DeepSeek Harness 的非官方桌面启动器：后台常驻、托盘、更新提示**

用 Tauri/Rust 构建的桌面壳应用，为上游 DeepSeek Harness（本身仅有 dsh web 浏览器 UI）补充三项能力：关闭窗口后宿主后台继续运行、托盘图标提供唯一真正的退出入口、启动时向 npm 查询新版本并提示安装（绝不自动）。应用不修改上游代码，按版本目录从 npm 消费上游，内置 Node.js（SHA-256 校验）、pnpm 与 harness 本体，安装后无需其他依赖。Windows/Linux 提供安装包，macOS 尚未构建。声明与 DeepSeek 无关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台常驻服务 + 托盘退出 + 手动更新提示三项补充功能
- 内置 Node.js/pnpm/harness，安装后无需额外依赖，首启离线
- 按版本目录消费上游，更新即目录切换，旧版本留作回滚
- 对上游零修改零 fork，界面即 harness 自带 web UI

## 适用场景

- 在桌面窗口而非浏览器中运行 DeepSeek Harness
- 关闭窗口后让进行中的任务继续在后台运行
- 通过统一入口安装并更新 harness 新版本

## 场景标签

 · 领域:AI agent 桌面工具

## 证据(README 行号)

> L5: Desktop launcher, background service and update prompt for
> L24: DeepSeek Harness ships a browser UI (`dsh web`) and nothing else: no desktop
> L31: |**Runs in the background**|The harness host keeps running when you close the window, so a task in flight is not ti

## 星数曲线

```mermaid
xychart-beta
    title "eshmeshek/deepseek-harness-desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `808ee45542e0` · [字段定义](../../DATASET.md)*
