# esimov/pigo

⭐ 4,747 · Go · MIT · 推送 2026-11-20 · [GitHub](https://github.com/esimov/pigo) · 个人维护

**纯 Go 的人脸检测、瞳孔定位与面部关键点检测库**

基于 Pixel Intensity Comparison-based Object detection 论文实现的纯 Go 库，提供人脸检测、平面内旋转人脸检测、瞳孔/眼睛定位与面部关键点检测。无需安装 OpenCV 或第三方模块，级联文件直接嵌入生成的二进制中，检测前不需图像预处理与积分图、图像金字塔等数据结构计算。提供 CLI 工具（支持 stdin/stdout 管道与 JSON 输出）、Go API、WASM 版本（README 称可达约 60 FPS），并可编译为共享对象供 Python 等语言调用。需要安装 Go 环境，或从 Releases 获取二进制，也可通过 snapcraft 获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Go 实现，不需要安装 OpenCV 或第三方模块
- 支持瞳孔/眼睛定位与面部关键点检测，级联文件嵌入二进制
- 支持 WASM，浏览器中实时人脸检测
- CLI 支持 stdin/stdout 管道与 JSON 检测结果输出

## 适用场景

- 在 Go 项目中做人脸与面部关键点检测而不想引入 cgo 依赖
- 浏览器端 WASM 实时人脸检测
- 命令行批量处理图片并输出检测坐标 JSON

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: Pigo is a pure Go face detection, pupil/eyes localization and facial landmark points detection library based on the 
> L19: - [x] Does not require OpenCV or any 3rd party modules to be installed
> L63: Starting from version **v1.4.0** the library has been ported to **WASM**. This proves the library's real time face 

## 星数曲线

```mermaid
xychart-beta
    title "esimov/pigo 星数(近 5 点)"
    x-axis ["2026-11-14", "2026-11-15", "2026-11-19", "2026-11-21", "2026-11-22"]
    y-axis "stars" 4741 --> 4748
    line [4742, 4743, 4744, 4747, 4747]
```

2026-11-14 4,742 → 2026-11-22 4,747（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `eb03fdc8e57b` · [字段定义](../../DATASET.md)*
