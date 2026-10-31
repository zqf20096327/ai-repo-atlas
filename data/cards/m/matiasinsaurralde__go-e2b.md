# matiasinsaurralde/go-e2b

⭐ 14 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/matiasinsaurralde/go-e2b) · 个人维护

**E2B 云沙箱的非官方 Go SDK：创建并管理安全 microVM**

以 Go 库形式封装 E2B 云沙箱 API，支持创建/列出沙箱、通过登录 shell 执行命令并流式读取输出、交互式 PTY 终端、文件系统读写、暂停/恢复与快照、一分为多的沙箱 Fork、持久卷挂载、出站网络策略与模板标签管理；错误以类型化错误（如 CommandExitError）返回。需要 Go 1.25+ 与 E2B API key，base 模板含 Python 3.11 与 Node.js 20。面向在 Go 程序中集成代码执行沙箱的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命令经登录 shell 执行，支持流式 stdout/stderr 与类型化退出码错误
- 沙箱暂停/恢复、快照与 Fork（克隆为多个独立副本）
- 持久卷、出站网络策略（allowlist）与 PTY 交互终端
- 通过 ClientConfig 字段或环境变量（E2B_API_KEY 等）配置

## 适用场景

- 在 Go 服务中为 AI agent 提供安全执行任意代码的环境
- 批量克隆沙箱并行分发任务并汇总结果
- 对沙箱出站网络做白名单限制以满足安全要求

## 场景标签

 · 领域:开发者工具/云沙箱

## 证据(README 行号)

> L10: A Go SDK for the E2B cloud sandbox API. E2B provides lightweight microVMs you can use to safely run arbitrary code 
> L20: - Go 1.25+

## 星数曲线

```mermaid
xychart-beta
    title "matiasinsaurralde/go-e2b 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `f8c9c592c35f` · [字段定义](../../DATASET.md)*
