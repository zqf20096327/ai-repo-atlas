# Martossien/transcria

⭐ 47 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Martossien/transcria) · 个人维护

**自托管会议转录门户：GPU 上产出校正稿、纪要与 Word 会议记录**

面向持续处理真实会议录音的团队的自托管 Web 服务（Flask + PostgreSQL，Docker 部署）：在自有 GPU 上完成语音转写、说话人分离（Nemotron/pyannote/MOSS 等）、LLM 纠正的 SRT 转录稿、结构化摘要、质量报告与按会议类型生成的 Word 会议记录，无云端 API 计费。提供人审向导、GPU 队列与调度、多用户角色访问、OIDC/LDAP 认证、GDPR 审计；支持单机与分布式 GPU 拓扑，含 8GB 显卡与 CPU-only 配置。界面与产出支持法/英，德/西/意为 beta。安装经 install.sh 或 Windows 11 脚本，另有浏览器内音频预检演示。参考质量依赖门控模型（gated models）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 转写 + 说话人分离 + LLM 校正 + 摘要 + Word 会议记录的全流程，含人审向导
- 多 STT 引擎（audio.cpp/parakeet.cpp/Voxtral/Kroko/MOSS 等），支持 8GB 显卡与 CPU-only 档位
- 对接 Jitsi/Zoom/Google Meet/Visio 平台仅出站连接即可定时录制，分轨转写各参与者
- OIDC/LDAP 单点登录、角色多用户、GDPR 审计与个人 API token

## 适用场景

- 团队每周批量把会议录音转成带说话人属性的校正稿和会议纪要
- 数据不出本地的合规场景下做转写与纪要生成
- 从 Jitsi/Zoom/Google Meet 日历自动录制并直接产出会议记录

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: **Self-hosted meeting transcription portal.** TranscrIA turns long meeting recordings into
> L15: usable deliverables on your own GPUs: corrected, speaker-attributed transcripts (SRT),
> L16: structured summaries, quality reports, and meeting-type-aware Word minutes. No cloud, no

## 星数曲线

```mermaid
xychart-beta
    title "Martossien/transcria 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-29 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cfa865e77818` · [字段定义](../../DATASET.md)*
