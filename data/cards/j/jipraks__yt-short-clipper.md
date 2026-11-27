# jipraks/yt-short-clipper

⭐ 1,114 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/jipraks/yt-short-clipper) · 个人维护

**面向内容创作者的 Windows 桌面应用：将长视频转为带字幕的 9:16 短视频剪辑**

Cuplik（原 YT Short Clipper v2）是 Windows 桌面应用，用户粘贴 YouTube URL 并提供 cookies.txt 后，由 yt-dlp 获取视频与字幕，LLM 读取转录文本挑选 58-120s 高光片段，切分后重构成 9:16 竖屏（MediaPipe 人脸追踪/居中/模糊填充三种模式），烧录逐词字幕并输出 MP4，可选通过 Repliz 上传与定时发布。技术栈为 React 19 + Tauri v2 + Python sidecar。仅支持 Windows，处于 beta 状态，版本间可能有破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 高光检测，支持任意 OpenAI 兼容端点及自由文本 AI 指令（时间范围、主题定向）
- MediaPipe 人脸追踪竖屏重构与逐词字幕烧录（使用 YouTube 原字幕，无需转录 API 或本地 Whisper）
- 内置钱包（QRIS 充值）或自带 API key 两种 AI 付费方式
- Repliz 直传与多账号定时发布，印尼语/英语界面

## 适用场景

- 把长 YouTube 视频批量切成可发布的竖屏短视频
- 为每个片段自动生成标题与描述并定时发布到多个账号
- 用自然语言指定时间段或主题来筛选剪辑内容

## 场景标签

`视频生成` `AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L36: Cuplik (formerly **YT Short Clipper v2**) is a Windows desktop app that turns a long-form
> L55: 3. An LLM reads the transcript and proposes highlight segments (58–120s by default).
> L61: - **AI highlight detection** from the video's subtitle transcript, via any

## 星数曲线

```mermaid
xychart-beta
    title "jipraks/yt-short-clipper 星数(近 24 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 1044 --> 1120
    line [1050, 1052, 1053, 1055, 1059, 1061, 1050, 1074, 1075, 1076, 1078, 1082, 1084, 1085, 1088, 1091, 1094, 1099, 1101, 1105, 1106, 1108, 1112, 1114]
```

2026-10-25 1,050 → 2026-11-27 1,114（+64）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `b28aed8c0efc` · [字段定义](../../DATASET.md)*
