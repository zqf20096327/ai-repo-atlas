# NguyenTriBaoThang/SafeHome3DAI

⭐ 3 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/NguyenTriBaoThang/SafeHome3DAI) · [官网](https://nguyentribaothang.github.io/SafeHome3DAI/) · 个人维护

**面向老年人居家跌倒风险评估的 AI 视觉与 3D 数字孪生平台**

Next.js 15 + Three.js 构建的 Web 应用，将居家跌倒风险管理组织为 7 步闭环流程：越南语自适应问卷调研、房间照片的多层视觉识别（18 类家具/障碍物分类、边界框标注、H1..H4 风险点标记）、基于 CDC STEADI 与 WHO 参考标准的确定性规则风险评分引擎、WebGL 3D 数字孪生场景与干预情景模拟、以及带引用来源的 RAG 问答助手。支持本地检测器或 Gemini 云端推理，含人工确认环节；明确声明结果为环境参考，不构成医学诊断。

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

- 18 类室内物体识别与风险点（H1..H4）影像标注，支持本地检测器或 Gemini 云端
- 确定性规则引擎（8 条规则）生成 0-100 分环境风险评分并可视化决策溯源链
- Three.js photorealistic dollhouse 数字孪生，含光照（0-520 Lux）与地面摩擦模拟
- Grounded RAG 助手带 4 标签证据抽屉，引用 WHO/NCOA/CDC 等来源

## 适用场景

- 家属上门用手机拍摄房间，识别地毯、电线、尖锐桌角等跌倒隐患
- 改造前用情景模拟器试算加装扶手、防滑垫后的评分变化
- 生成含费用预算的适老化改造清单并导出 PDF 报告
- 通过 RAG 助手查询 WHO/CDC 跌倒预防依据原文

## 场景标签

`RAG` `目标检测` · 领域:知识与检索

## 证据(README 行号)

> L69: 2. **Thị giác máy tính đa tầng**: Quét không gian toàn cảnh phòng (`/ai-vision`) và **Hỗ trợ đánh giá yếu tố nguy c
> L71: 4. **Động cơ luật hỗ trợ đánh giá yếu tố môi trường (Deterministic Rules)** tham chiếu WHO 2021 & CDC STEADI. Kết q
> L146: - **Xử lý ảnh gia đình & Camera thiết bị (`LiveCameraCaptureModal`):** Hỗ trợ cả tải ảnh thực tế (`JPG`, `PNG`, `W


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `2dec9611e7fd` · [字段定义](../../DATASET.md)*
