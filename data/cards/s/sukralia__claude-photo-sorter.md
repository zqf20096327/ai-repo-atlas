# sukralia/claude-photo-sorter

⭐ 4 · JavaScript · MIT · 推送 2026-11-15 · [GitHub](https://github.com/sukralia/claude-photo-sorter) · [官网](https://github.com/sukralia/claude-photo-sorter) · 个人维护

**让 Claude 读取本地照片文件夹并自动分类与去重的桌面工具**

面向旅行归来有大量照片的普通用户：通过 Claude 桌面应用的 Code 功能安装运行，由后台 Claude Code 进程（claude -p，并发 4 个）查看照片缩略图并分配文件夹，将照片和视频分类到自拍、人物、食物、截图等目录；通过文件指纹比对找出重复项并放入 _Review 文件夹。只读取原件并生成排序副本，不移动原件，全部处理在本机进行。需要 Claude Pro 或 Max 订阅，受用量限制，达限后暂停并可续跑。需 Python 3.9+，Mac/Windows/Linux 可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按类别生成排序副本，不改动原件，Mac 上副本不占额外空间
- 指纹比对加像素检查识别重复、连拍与重复截图
- 浏览器仪表盘提供进度、浏览、改判与自定义文件夹
- 内置假照片演示模式，无需真实照片即可预览

## 适用场景

- 整理旅行后堆积的几千张照片和视频
- 找出重复照片并人工确认保留哪一份
- 本机处理照片、不上传任何原始文件

## 场景标签

`图像视频处理` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: **Back from a trip with 2,000 photos and no idea what's in there? Point Claude at the folder and watch every photo f
> L63: 3. **Claude looks**: runs Claude Code in the background (`claude -p`), four at a time, each looking at contact shee

## 星数曲线

```mermaid
xychart-beta
    title "sukralia/claude-photo-sorter 星数(近 3 点)"
    x-axis ["2026-11-20", "2026-11-23", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-20 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `5cc26ca4c6b8` · [字段定义](../../DATASET.md)*
