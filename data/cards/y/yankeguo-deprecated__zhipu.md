# yankeguo-deprecated/zhipu

⭐ 41 · Go · MIT · 推送 2026-07-03 · [GitHub](https://github.com/yankeguo-deprecated/zhipu) · [官网](https://bigmodel.cn/dev/api/libraries) · 个人维护 · 中文 README

**智谱 AI 平台的第三方 Go 客户端库**

非官方的 Golang 包，封装智谱 AI 开放平台 API：支持 ChatCompletion（含流式与 GLM-4-AllTools 工具调用）、Embedding、CogView 图像生成、CogVideoX 视频生成、文件上传（检索/微调用途）、Batch 批量任务、知识库与微调任务管理，并附批量文件写入/结果读取的辅助工具。客户端通过 API key（环境变量或参数）创建。面向在 Go 项目中接入智谱平台的开发者，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatCompletion 普通与流式调用，支持 GLM-4-AllTools 工具调用
- 覆盖图像生成、视频生成、Embedding、文件上传、Batch、知识库、微调等接口
- 提供 BatchFileWriter / BatchResultReader 批量辅助工具

## 适用场景

- 在 Go 服务中接入智谱 GLM 系列模型完成对话与流式输出
- 通过代码调用 CogView/CogVideoX 生成图像与视频
- 用 Go 管理智谱平台的批量任务、知识库与微调

## 场景标签

`图像生成` `视频生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L9: A 3rd-Party Golang Client Library for Zhipu AI Platform
> L16: go get -u github.com/yankeguo/zhipu

## 星数曲线

```mermaid
xychart-beta
    title "yankeguo-deprecated/zhipu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e60cb3473a0a` · [字段定义](../../DATASET.md)*
