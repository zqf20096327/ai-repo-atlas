# wanikua/byebyeclaw

⭐ 75 · Shell · MIT · 推送 2026-03-15 · [GitHub](https://github.com/wanikua/byebyeclaw) · 个人维护 · 中文 README

**一键卸载所有 Claw 家族 AI Agent 的清理脚本，无残留**

面向安装过多个 Claw 家族 AI Agent（OpenClaw、NanoBot、ZeroClaw、IronClaw 等 12 种）的用户的卸载清理工具。以 shell 脚本（macOS/Linux）与 PowerShell 脚本（Windows）形式通过 curl/irm 一行命令运行，按 15 个维度扫描并删除：包管理器全局包、二进制、配置与缓存目录、systemd/launchd 服务、Docker 容器与镜像、VS Code 扩展、crontab、运行中进程、shell 配置残留等。提供 --dry-run 预览、--keep-config、--select 交互选择与中英文界面选项。删除前列出清单并确认，不影响无关工具。

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

- 一行命令卸载 12 种 Claw 家族 AI Agent 及其数据
- 15 个扫描维度覆盖包管理器、服务、Docker、VS Code 扩展、shell 配置等
- 提供 --dry-run / --keep-config / --select 选项，删除前列出清单并确认
- macOS/Linux shell 与 Windows PowerShell 双脚本，自动检测中英文

## 适用场景

- 试用过多个 Claw 系 Agent 后清理散落的配置和全局包
- 卸载前用 --dry-run 预览将被删除的内容
- 清理 Docker 容器、系统服务与 shell 配置中的 Agent 残留

## 场景标签

 · 领域:开发者工具/系统清理

## 证据(README 行号)

> L8: **One command to uninstall ALL Claw-family AI agents. Zero residue.**
> L10: Tried OpenClaw, ZeroClaw, NanoClaw, IronClaw and forgot to clean up? Config dirs scattered everywhere, npm globals 
> L34: |OpenClaw|300k⭐|The original personal AI assistant|

## 星数曲线

```mermaid
xychart-beta
    title "wanikua/byebyeclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-28 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fff3cd587397` · [字段定义](../../DATASET.md)*
