# 2005selene2005-a11y/susu-phone-agent

⭐ 39 · Java · MIT · 推送 2026-08-22 · [GitHub](https://github.com/2005selene2005-a11y/susu-phone-agent) · 个人维护

**通过 MCP + Shizuku 让 Claude Code 控制真实 Android 设备的桥接工具**

由三部分组成：本机运行的 FastMCP stdio 服务器（Claude Code 以 MCP 工具调用）、自托管 FastAPI 任务队列（Phone Bridge）、Android 前台服务 APK（借助 Shizuku 无线 ADB 模式，无需 root）。手机通过普通 HTTPS 轮询 Bridge 拉取任务，设备上不做任何 AI 推理，也不接收 Claude 凭据；反向连接方式适配 NAT 与移动数据环境。MCP 暴露白名单工具面，包名经正则校验；可选 Sleep Guard 规则引擎按封禁列表按 HOME 键。构建 APK 需 JDK 17+ 与 Android SDK API 34。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP + Shizuku 的三组件架构，无需 root、设备不做 AI 推理
- 手机反向轮询自托管 Bridge，适配 NAT/移动数据，不在手机上存 Claude 凭据
- 白名单工具面：无任意 executeShell，launch_app 包名正则校验
- 可选 Sleep Guard 本地规则引擎（默认关闭，双重开关）

## 适用场景

- 让 Claude Code 操作我的真机完成打开应用、回主屏等指令
- 跨网络（NAT/移动数据）远程控制 Android 设备
- 限制特定应用使用的家长式看护场景（Sleep Guard）

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L37: **1. Phone MCP** (`mcp/phone_mcp.py`) — a FastMCP stdio server. Claude Code calls it like any other MCP tool. It fo
> L41: **3. Android Agent APK** (`android/`) — a foreground service. Built with Shizuku in wireless ADB mode. No root requ

## 星数曲线

```mermaid
xychart-beta
    title "2005selene2005-a11y/susu-phone-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a4e31688082c` · [字段定义](../../DATASET.md)*
