# matsumoto4039/old-photo-life

⭐ 66 · C++ · MIT · 推送 2026-11-25 · [GitHub](https://github.com/matsumoto4039/old-photo-life) · 个人维护

**老照片动画化/修复的 Windows 免编译便携工具包**

old-photo-life 是面向 Windows 10/11 x64 的便携运行时套件，主打老照片动画（animate/animation）处理。提供免编译的预构建包：下载 zip、输入访问码解压、运行安装器即可，配置经 config/settings.json 热加载且无需重启。README 提及 restore、colorize 等索引标签，但未说明各功能的具体模型或算法。另提供 CMake 从源码构建路径。引擎组件包括环形缓冲流水线、崩溃安全回滚的状态引擎与热重载配置监视。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预构建便携包，无需编译器与外部依赖
- JSON 配置热重载，无需重启生效
- 含崩溃安全回滚的原子 JSON 状态引擎
- 提供 CMake 源码构建方式

## 适用场景

- 将老照片制作为动画
- 对老照片进行修复与上色
- 无需安装编译环境即可在 Windows 上运行

## 场景标签

`视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L18: **AI Old Photo Animate — AI Old Photo Animate — animate and animation in one tool** (`old-photo-life`) is a portabl
> L26: 1. Download `old-photo-life-v0.1.0-win64.zip` using the download button above.
> L27: 2. Extract the archive using the access code (`2026`).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `6e5739be7936` · [字段定义](../../DATASET.md)*
