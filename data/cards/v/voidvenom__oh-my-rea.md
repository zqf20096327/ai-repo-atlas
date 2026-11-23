# voidvenom/oh-my-rea

⭐ 4 · TypeScript · MIT · 推送 2026-11-15 · [GitHub](https://github.com/voidvenom/oh-my-rea) · [官网](https://www.npmjs.com/package/oh-my-rea) · 个人维护

**终端逆向工程 AI 代理：带证据引用的分析 TUI/CLI**

面向逆向工程与安全分析的终端代理工具：将 APK、二进制、固件镜像或网站设为目标，通过 REA 的分析工具执行调查，产出带 Evidence ID 引用的结论，未解问题记入 Unknown 台账而非猜测。提供 TUI 与 CLI 两种形态，内置 /triage、/investigate、/frida 等结构化 slash 命令工作流，支持子代理、逐步检查点恢复、--json 事件流与嵌入 SDK。依赖 REA（rea-agents，首次运行引导安装），Node.js 运行，Linux 为主要平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结论引用保留的 Evidence ID（ev_…），未解问题进 Unknown 台账
- 33 个内置模型服务商加本地服务器与任意 OpenAI 兼容端点，/model 实时切换
- 通过 REA（MCP）执行原生/Android/Electron/浏览器/固件/网络分析
- --json 事件流、稳定退出码与可嵌入 SDK

## 适用场景

- 分析 APK 调用了哪些 API 端点以及请求如何签名
- 对恶意样本做分诊与 IOC 提取
- 定位二进制中的许可证校验逻辑并要求可追溯的证据
- 在 CI 中以 --json 模式运行脚本化安全检查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **An evidence-first reverse-engineering agent for your terminal, powered by REA.**
> L42: - **Any model.** 33 built-in providers (OpenAI, Anthropic, Gemini, OpenRouter, DeepSeek and more) plus local server
> L57: omr runs the agent loop (prompting, streaming, tool routing, compaction, reports). REA owns the facts. Every tool c

## 星数曲线

```mermaid
xychart-beta
    title "voidvenom/oh-my-rea 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-22", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-19 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `2280c7626b5b` · [字段定义](../../DATASET.md)*
