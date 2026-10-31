# lasermaze/Cellar

⭐ 15 · Swift · MIT · 推送 2026-05-05 · [GitHub](https://github.com/lasermaze/Cellar) · 个人维护

**用 AI agent 自动配置 Wine、在 Mac 上运行老 Windows 游戏的工具**

macOS 上的免费开源工具，提供 Web UI 与 CLI，通过 AI agent 自动完成 Wine 配置并运行老 Windows 游戏（Apple Silicon 与 Intel 均支持）。agent 按 Research-Diagnose-Adapt 三阶段循环工作：查询本地成功数据库与社区集体记忆、检索 WineHQ/ProtonDB/PCGamingWiki，运行带调试追踪的诊断性启动，再施加并验证修复；拥有 20+ 工具（DLL 追踪、PE 导入检查、已知 DLL 下载、注册表编辑等）。支持 Claude/DeepSeek/Kimi 三类 API key，无 key 时退回仅配方模式。一行脚本安装预编译通用二进制，也可从源码构建；自动安装 Homebrew、Wine、winetricks 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Research-Diagnose-Adapt 三阶段 AI agent 自动诊断并修复兼容问题（20+ 工具）
- 接受 .exe 安装包与 .iso/.bin/.cue 光盘镜像，自动挂载
- 工作配置保存为本地配方并可经社区集体记忆共享
- 每游戏独立 Wine bottle 隔离运行，agent 只能修改该 bottle 内文件

## 适用场景

- 在 Mac 上运行 GOG/光盘/老 PC 游戏而无需手动调 Wine
- 让 AI agent 自动处理 DLL 覆盖、注册表与 DirectDraw/Direct3D 配置
- 通过本地 Web UI 管理游戏库并查看 agent 实时日志

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Cellar is a free, open-source macOS tool with both a **web UI** and **CLI** that uses an AI agent to automatically c
> L26: > **You need an API key to use the AI agent.** Without one, `cellar launch` falls back to recipe-only mode (no auto
> L69: - An AI API key (Anthropic, Deepseek, or Kimi) for the AI agent — without one, Cellar falls back to recipe-only lau

## 星数曲线

```mermaid
xychart-beta
    title "lasermaze/Cellar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b6f2b725eaed` · [字段定义](../../DATASET.md)*
