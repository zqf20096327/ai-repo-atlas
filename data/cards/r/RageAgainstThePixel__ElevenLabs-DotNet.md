# RageAgainstThePixel/ElevenLabs-DotNet

⭐ 99 · C# · MIT · 推送 2026-03-09 · [GitHub](https://github.com/RageAgainstThePixel/ElevenLabs-DotNet) · [官网](https://try.elevenlabs.io/rage-against-the-pixel) · 个人维护

**.NET 8 的 ElevenLabs TTS/配音 API 非官方客户端库**

面向 .NET 开发者的 ElevenLabs RESTful API 非官方客户端库，以 NuGet 包分发，目标框架 .NET 8.0 及以上，可在控制台、WinForms、WPF、ASP.NET 等项目类型中使用。封装文本转语音（含流式）、语音列表与管理（增删改、克隆样本）、音视频配音（含转写 SRT 导出）、音效生成、历史记录与用户/订阅信息查询等端点。支持三种 API key 提供方式（构造函数、配置文件 .elevenlabs、环境变量），并另行提供 ElevenLabs-DotNet-Proxy 包用于在前端应用与 ElevenLabs 之间架设 ASP.NET Core 代理以保护密钥；另有 Unity 的 OpenUPM 包。需要 ElevenLabs 账号与 API 权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 TTS/流式 TTS、语音管理与克隆样本、配音（含 SRT 转写）、音效生成、历史与用户端点
- 三种 API key 认证方式：构造函数、配置文件、环境变量
- ElevenLabs-DotNet-Proxy 包提供 ASP.NET Core 中间代理以避免前端暴露密钥
- 支持 Windows/Linux/Mac 与多种 .NET 项目类型，另有 Unity OpenUPM 包

## 适用场景

- 在 .NET 应用中集成 ElevenLabs 文本转语音或音效生成
- 为 Unity 游戏接入 ElevenLabs 语音合成
- 通过自建代理服务安全地向客户端转发 ElevenLabs 请求
- 用 .NET 代码批量管理 ElevenLabs 语音与配音项目

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L9: A non-official Eleven Labs voice synthesis RESTful client.
> L25: Install package `ElevenLabs-DotNet` from Nuget. Here's how via command line:

## 星数曲线

```mermaid
xychart-beta
    title "RageAgainstThePixel/ElevenLabs-DotNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 98 --> 100
    line [99, 99]
```

2026-10-18 99 → 2026-10-29 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `291d67599150` · [字段定义](../../DATASET.md)*
