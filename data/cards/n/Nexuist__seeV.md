# Nexuist/seeV

⭐ 34 · Swift · 推送 2026-08-12 · [GitHub](https://github.com/Nexuist/seeV) · 个人维护

**macOS 命令行工具：在 shell 中调用 Apple Vision 做图像/视频识别**

用 Swift 编写的 macOS 命令行程序，封装 Apple Vision 框架，供 shell 脚本与其他命令行工具对图像和视频执行检测：主体提取、人脸/人体/姿态检测、OCR、图像分类、嵌入与相似度、质量评分、SHA-1 哈希；帧级命令自动识别视频并按时间均匀采样。多数操作无网络与运行时依赖，仅 nsfw 审核需本地 Ollama 与 ShieldGemma 2 模型。要求 macOS 15 以上，提供 M1 构建下载或源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人脸/人体/姿态检测与 OCR，结果以 JSON 输出并含边界框与置信度
- 图像嵌入与余弦相似度距离计算、审美质量评分、SHA-1 去重哈希
- 视频输入自动按时间均匀采样最多指定帧数进行分析
- nsfw 审核经本地 Ollama 调用 ShieldGemma 2，默认图像不离开本机

## 适用场景

- 在 shell 脚本中批量检测图片中的人脸、人体或文字
- 给图片库做相似度比较、质量评分与去重
- 对视频抽样帧做内容检测与本地 NSFW 审核

## 场景标签

`目标检测` `OCR` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: seeV is a macOS command line wrapper around the Apple Vision framework. Its goal is to unlock the functionality of t
> L7: ## Supported Operations
> L25: seev faces input.jpg -o output.png

## 星数曲线

```mermaid
xychart-beta
    title "Nexuist/seeV 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1907296470e4` · [字段定义](../../DATASET.md)*
