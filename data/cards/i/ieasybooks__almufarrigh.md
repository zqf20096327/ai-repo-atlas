# ieasybooks/almufarrigh

⭐ 15 · QML · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ieasybooks/almufarrigh) · 个人维护

**跨平台语音转写工具的 Qt 图形界面（桌面端）**

基于 Python 与 Qt（PySide6）的桌面图形界面，用于包装语音/视频转写工具，面向需要在 Windows/macOS/Linux 上以图形方式运行转写的用户，仓库标签含 whisper、subtitles、audio-processing、video-processing。运行方式为：在 src 目录用 pyside6-rcc 编译资源文件（或运行 update_resources.bat），随后执行 python main.py。README 仅包含运行步骤，未给出打包安装包或依赖清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PySide6 图形界面，运行于 Windows/macOS/Linux 桌面系统
- 用于操作语音/视频转写（标签含 whisper 与 subtitles）
- 提供资源编译命令与 Windows 批处理脚本两种准备方式

## 适用场景

- 在桌面系统上以图形界面运行语音转写工具
- 将音频/视频内容转写为字幕文本

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L5: الواجهة الرسومية الخاصة بأداة تفريغ على أنظمة التشغيل المختلفة
> L9: نفذ الأمر التالي في داخل المجلد `src` لتوليد ملف الموارد

## 星数曲线

```mermaid
xychart-beta
    title "ieasybooks/almufarrigh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `977b7fe491c7` · [字段定义](../../DATASET.md)*
