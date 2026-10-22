# rodrigogs/whats-reader

⭐ 274 · TypeScript · AGPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/rodrigogs/whats-reader) · [官网](https://rodrigogs.github.io/whats-reader/) · 个人维护 · 中文 README

**离线浏览 WhatsApp 聊天导出文件的桌面/网页应用，含本地语音转写**

面向 WhatsApp 用户的隐私优先应用：拖入手机导出的聊天 .zip 文件，即可在本地浏览消息、照片与语音，支持全文搜索、书签、多视角模式、统计图表与媒体画廊批量下载。语音消息通过 Whisper 模型在浏览器内经 WebGPU 本地转写，支持 12+ 种语言，无需服务器与 API key。数据全程不离开设备，零遥测。基于 SvelteKit 与 Electron 构建，提供 Windows/macOS/Linux 安装包及免安装网页版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 经 WebGPU 在浏览器内本地转写语音（12+ 语言，无需 API key）
- 媒体画廊按日期组织照片/视频/音频，可批量选择下载为 ZIP
- 全文搜索、书签（JSON 导入导出）、任意参与者视角、统计图表
- 三平台安装包与网页版，支持 10 种界面语言

## 适用场景

- 在电脑上翻阅备份的 WhatsApp 聊天记录而不上传数据
- 把语音消息转成文字再搜索
- 统计聊天活跃度并批量导出媒体文件

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L35: Drop a WhatsApp `.zip` export and browse your messages, photos, and voice notes. Works with big chats (tested with 
> L39: Voice messages can be transcribed using Whisper, which runs in your browser via WebGPU. No server, no API key neede
> L102: - **Voice transcription**: Transcribe audio with Whisper (runs locally, 12+ languages)

## 星数曲线

```mermaid
xychart-beta
    title "rodrigogs/whats-reader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 273 --> 276
    line [274, 275, 274]
```

2026-10-18 274 → 2026-10-22 274（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4fd1ea864941` · [字段定义](../../DATASET.md)*
