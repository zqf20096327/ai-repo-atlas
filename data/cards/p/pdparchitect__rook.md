# pdparchitect/rook

⭐ 35 · Go · MIT · 推送 2026-08-24 · [GitHub](https://github.com/pdparchitect/rook) · 个人维护

**给安全研究者的自主 AI 漏洞挖掘 harness（单一 Go 二进制）**

面向漏洞研究、bug 挖掘与源码审计的自主 AI 工具：用户以 YAML 目标文件定义任务与成功标准，内置的自主引擎 zot 在单二进制内运行，通过 OpenAI 兼容接口连接任意提供方（默认 zai 的 glm-5.2，支持 Anthropic、本地 Ollama、网关、自定义端点），自带 API key、无托管服务与遥测。提供可恢复会话、任务台账、watch 模式与按需技能目录。README 声明为攻击性安全工具，仅限授权使用，并标注 0.x 阶段行为可能变更。安装经 install.sh 脚本获取 Linux/macOS amd64/arm64 发布二进制，或从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 目标文件驱动：队列、批量、流式任务与完成台账
- 单一静态 Go 二进制，跨平台，可携带到目标机器后清理
- 兼容任意 OpenAI 兼容提供方，含本地 Ollama 与自定义网关
- 可恢复会话、循环检测、压缩与按需技能目录

## 适用场景

- 授权范围内对自有代码做注入与鉴权绕过等漏洞审计
- 无人值守跑安全研究目标，回来查看带回证据的发现
- 用本地或自有 API key 的模型进行源码安全排查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: Rook is an AI bug-hunting harness for vulnerability research, bug hunting and
> L12: back them. The autonomous engine (zot) runs
> L13: inside the binary and talks straight to any OpenAI-compatible provider with your

## 星数曲线

```mermaid
xychart-beta
    title "pdparchitect/rook 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `63ae373774b0` · [字段定义](../../DATASET.md)*
