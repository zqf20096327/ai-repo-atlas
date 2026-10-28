# nihui/ncnn-webassembly-nanodet

⭐ 133 · C++ · 推送 2026-10-27 · [GitHub](https://github.com/nihui/ncnn-webassembly-nanodet) · [官网](https://nihui.github.io/ncnn-webassembly-nanodet/) · 个人维护 · 中文 README

**在浏览器中用 ncnn+WebAssembly 运行 nanodet 目标检测**

基于 Tencent ncnn 官方 WebAssembly 预编译 SDK 与 Emscripten 构建的网页端目标检测 demo，模型为 nanodet-plus（参考 ncnn 官方 nanodetplus_pnnx 示例修改为 Web 版）。同时构建 wasm32 与 wasm64 的 basic、SIMD、threads、SIMD+threads 共八种变体，页面自动选择浏览器支持的变体并在支持 Memory64 时优先 wasm64，不支持时回退 wasm32。构建需 CMake 3.13+，通过摄像头取流进行检测，线程变体需配置跨域隔离响应头。提供在线 demo 页面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八种 wasm 变体（wasm32/wasm64 × basic/SIMD/threads/SIMD+threads）自动检测与回退
- 基于 ncnn 官方 WebAssembly 预编译 SDK，无需从源码编译 ncnn
- 浏览器内摄像头实时目标检测（nanodet-plus）
- 线程变体使用最多四个 pthread（一个推理 worker 与最多三个 OpenMP worker）

## 适用场景

- 在浏览器中体验 ncnn + nanodet 目标检测效果
- 参考其构建流程开发自己的 ncnn WebAssembly 应用
- 测试不同 wasm 特性（SIMD/threads/Memory64）在浏览器中的表现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: 参考 https://github.com/Tencent/ncnn/blob/master/examples/nanodetplus_pnnx.cpp 修改了 nanodet-plus 版本的 Web 版
> L9: open https://nihui.github.io/ncnn-webassembly-nanodet and enjoy


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `259e3aa2605d` · [字段定义](../../DATASET.md)*
